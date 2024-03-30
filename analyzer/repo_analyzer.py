import socket
from pydriller import Repository
from tqdm import tqdm
import nltk
import csv
import json
import os
import datetime
import requests
import logging
import torch
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import hashlib

# Download the necessary NLTK models (run once)
nltk.download('punkt')


MAX_COMMIT = 500  #define max number of commits to be collected, uncomment if not necessary

# Initialize a global batch_id
batch_id = 0
seen_hashes = set()
total_found = 0
repo_counter_success = 0
repo_counter_fail = 0

# Disable tokenizers parallelism
os.environ["TOKENIZERS_PARALLELISM"] = "false"
cpu_count = os.cpu_count()

# Load the tokenizer and model only once

tokenizer = AutoTokenizer.from_pretrained("ManojAlexender/Research_paper_MLM_all_CGO_Level_2_Final_Model_V1")
model = AutoModelForSequenceClassification.from_pretrained("ManojAlexender/Research_paper_MLM_all_CGO_Level_2_Final_Model_V1")



 # Check if GPU (CUDA) is available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Move model to the chosen device
model.to(device)

# root for the script

root_dir = "miner_github/analyzer"

data_threshold = 500
commit_data = [] # running commit buffer


# def setup_logging():
#     '''
#     # Function to initialize logging
#     '''
#     logs_dir = os.path.join(root_dir, "logs")  # Log directory
#     os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists
#     log_file_path = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
#     logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Logging configuration
logs_dir = os.path.join(root_dir, "logs") #log directory
os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists
log_file_path = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info(f"Using device {device}")

# use the loaded model to predict classificaiton
def get_prediction(input_text):
    """
    Accepts input_text and predicts 3 classes: LABEL_0, LABEL_1(Perf) or LABEL_2 
    """
    
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt",truncation=True, max_length=512)
    # Move the input tensors to the same device as the model
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        logits = model(**inputs).logits
    
   
    predicted_class_id = logits.argmax().item()
    predicted_label = model.config.id2label[predicted_class_id]
    return predicted_label


def get_ip_from_sshosts(sshosts_path):
    try:
        # Get the current node's hostname
        hostname = socket.gethostname()
        with open(sshosts_path, 'r') as file:
            for line in file:
                line_hostname, ip_address = line.strip().split()
                if line_hostname == hostname:
                    return ip_address
    except Exception as e:
        logging.error(f"Error reading from sshosts: {e}")
        return None

def get_public_ip(sshhosts_path='../sshhosts_hostname'):
    ip_address = get_ip_from_sshosts(sshhosts_path)
    if ip_address:
        logging.info(f"fetched IP locally!")
        return ip_address
    
    # If that fails, fall back to the API method
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching public IP: {e}")
        return "ErrorFetchingIP"

def count_tokens_code(code):
    tokens = nltk.word_tokenize(code)
    # Filter or process tokens as needed
    return len(tokens)


# Create a 'results' directory if it doesn't exist
results_dir = f'{root_dir}/results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)    


def read_repository_urls_from_csv(input_csv_file):
    logging.info(f"Processing input filename: {input_csv_file}")
    with open(input_csv_file, 'r') as input_file:
        reader = csv.reader(input_file)
        next(reader, None)  # Skip the header row
        repo_urls = {row[6] for row in reader}
    return list(repo_urls)


def write_commit_data_to_file():
    '''
    Function to write commit data to a new .jsonl file for each batch, using batch_id
    '''
    global commit_data
    # Generate filename using the batch_id
    filename = os.path.join(results_dir, f"batch_{batch_id}.jsonl")
    
    with open(filename, 'w') as file:  # Write mode
        for commit_info in commit_data:
            file.write(json.dumps(commit_info) + '\n')
    commit_data.clear()  # Clear the list after writing

def mine_repo_commits(repo_url, file_types=['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx']):
    global seen_hashes
    global batch_id
    global total_found
    global commit_data
    global data_threshold
    global repo_counter_fail
    global repo_counter_success
    local_commit_counter = 0
    start_time = time.time()  # Record the start time for the current repository

    try:
        for commit in Repository(repo_url, only_no_merge=True, only_modifications_with_file_types=file_types).traverse_commits():
            try:
                commit_message = commit.msg.lower().replace('\n', ' ')
                if len(commit.modified_files) == 1 and get_prediction(commit_message) == 'LABEL_1':
                    modified_file = commit.modified_files[0]

                    if modified_file.change_type not in ["ADD", "DELETE"]:
                        if len(modified_file.changed_methods) == 1:
                            if 'merge' in commit_message:
                                logging.info(f"Skipping merge commit: {commit.hash}")
                                continue
                            # get commit hash

                            # original source code
                            src_original = modified_file.source_code_before or "na"
                            src_modified = modified_file.source_code or "na"
                            key = src_original + src_modified # the idea is comes from disticnt traning data sicne we pass this code, so focus on it
                            #deduplicate based on this

                            key_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
                            if key_hash in seen_hashes:
                                logging.info(f"Skipping duplicate commit: {commit.hash}")
                                continue
                            #now proceed, extract info for this commit which met all our critera
                            # get changed method name
                            changed_method_name = modified_file.changed_methods[0].name
                            # get the commmit url
                            commit_url = repo_url
                            # get hash 
                            sha = commit.hash
                            # get filename
                            filename = modified_file.filename
                            # get changed method's location
                            changed_method_loc_start = modified_file.changed_methods[0].start_line
                            changed_method_loc_end = modified_file.changed_methods[0].end_line
                            loc_changed_method = f'[{changed_method_loc_start}:{changed_method_loc_end}]'
                            # get the list of methods in this file
                            methods = modified_file.methods_before
                            # now iterate through these methods to extract original version
                            # of the changed_method
                            for func in methods:
                                if func.name == changed_method_name:
                                     orig_method_loc_start = func.start_line
                                     orig_method_loc_end = func.end_line
                                     break
                            loc_orig_method = f'[{orig_method_loc_start}:{orig_method_loc_end}]'
                            
                            #get tokens in file
                            file_tokens = modified_file.token_count
                            n_loc = modified_file.nloc
                            n_added_lines = modified_file.added_lines
                            n_deleted_lines = modified_file.deleted_lines
                            # its time to concat all these info
                            commit_info = {
                                'commit_url': commit_url + '/commit/' + commit.hash,
                                'commit_message': commit_message,
                                'filename': filename,
                                'commit_date': str(commit.committer_date),
                                'no_tokens': file_tokens,
                                'nloc': n_loc,
                                'n_added_lines': n_added_lines,
                                'n_deleted_lines': n_deleted_lines,
                                'modified_method': changed_method_name,
                                'loc_before': loc_orig_method,
                                'loc_after': loc_changed_method,
                                'src_before': src_original,
                                'src_after': src_modified
                            }
                            # add this commit info to running list
                            commit_data.append(commit_info)
                            # mark it seen to avoid duplicate
                            seen_hashes.add(key_hash)
                            total_found += 1
                            local_commit_counter += 1
                            logging.info(f"Total found: {total_found}")

                            if len(commit_data) == data_threshold:
                                batch_id += 1
                                write_commit_data_to_file()
            except Exception as commit_error:
                logging.error(f"Error processing commit '{commit.hash}' in repository '{repo_url}': {commit_error}")
                # Continue to the next commit despite the error
                continue
        repo_counter_success += 1
    except Exception as repo_error:
        repo_counter_fail += 1
        logging.error(f"Error while accessing repository '{repo_url}': {repo_error}")
        
        # Continue to the next repository despite the error

    finally:
        end_time = time.time()  # End time for the current repository
        time_taken = end_time - start_time
        logging.info(f"Time taken for processing {repo_url}: {time_taken} seconds")
        logging.info(f"local_commit_found: {local_commit_counter} {repo_url}")



def main():
    global batch_id
    global total_found
    global commit_data
    global repo_counter_fail
    global repo_counter_success
    logging.info("Starting mining..")

    host_ip = get_public_ip()
    date = datetime.date.today().strftime("%m%d%Y")
    
    # here we read the .csv file containg this node's split of the repo list to be mined
    input_csv_file = os.path.join(root_dir, f"github_repositories_{host_ip}.csv")
    repo_urls = read_repository_urls_from_csv(input_csv_file)
    #repo_urls = ['https://github.com/opencv/opencv']  # List of repository URLs to process

    # process all the repositories in the list
    repo_counter = 0

    total_repo = len(repo_urls)
    
    time_start = time.time()
    for repo_url in repo_urls:
        repo_counter += 1
        logging.info(f"[{repo_counter}/{total_repo}]Processing reopository: {repo_url}")
        try:
            #analyze_repository(repo_url, output_csv_file_patterns1)
            mine_repo_commits(repo_url)
        except Exception as e:
            logging.error(f"Error processing this repository, continueing {repo_url}: {e}")
            continue
        if total_found > MAX_COMMIT:
            logging.info("Exiting analysis!")
            break
        

    logging.info(f"Writing remaining commit data if any")
    #remaining data if any
    if commit_data:
        logging.info(f"Found remaining {len(commit_data)} commit rows")
        batch_id += 1
        write_commit_data_to_file()
    time_finish = time.time()
    total_time = time_finish - time_start
    minutes, seconds = divmod(total_time, 60)
    logging.info(f"Analysis is complete!. Creating poll text file..")
    
    # record summary
    logging.info(f"Total repository: {total_repo}")
    logging.info(f"Total successfully processed: {repo_counter_success}")
    logging.info(f"Total failed to process: {repo_counter_fail}")
    logging.info(f"Total commit curated: {total_found}")
    logging.info(f"Total time taken: {int(minutes)}")
    # Command to execute
    command = 'touch miner_github/analyzer/script_complete.txt'

    # Execute the command
    result = os.system(command)

    if result == 0:
        logging.info(f"File 'script_complete.txt' created successfully.")
    else:
        logging.info(f"Failed to create file 'script_complete.txt'.")


if __name__ == "__main__":
    main()
