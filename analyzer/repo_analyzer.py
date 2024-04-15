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
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig #mistral

import hashlib
import oci # for oracle object store 
from oci.object_storage import ObjectStorageClient


# Download the necessary NLTK models (run once)
nltk.download('punkt')
hostname = socket.gethostname()

# OCI object store INFO
namespace = 'idqgqghww6tn'
bucket_name = 'bucket-20240414-1634'


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


## ML Model related ##
def parse_output(text):
    res = re.search(r'\b(Yes|No)\b', text)
    if res:
        return res.group(0)
    else:
        return None
    
 # Check if GPU (CUDA) is available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# ##### Roberta ########
# # Load the tokenizer and model only once

# tokenizer = AutoTokenizer.from_pretrained("ManojAlexender/Research_paper_MLM_all_CGO_Level_2_Final_Model_V1")
# model = AutoModelForSequenceClassification.from_pretrained("ManojAlexender/Research_paper_MLM_all_CGO_Level_2_Final_Model_V1")
# # Move model to the chosen device
# model.to(device)

# #### Roberta Ends #####

#### Mistral #####
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True, # Enables loading the model in 4-bit precision
    bnb_4bit_quant_type="nf4", # Specifies the quantization type
    bnb_4bit_use_double_quant=True, # Enables double quantization for better precision
)
# Loading the tokenizer
tokenizer = AutoTokenizer.from_pretrained("/home/ubuntu/Mistral-7B-Instruct-v0.2")
# Loading the model with BitsAndBytes configuration, and additional settings from Method-1
model = AutoModelForCausalLM.from_pretrained(
    "/home/ubuntu/Mistral-7B-Instruct-v0.2",
    torch_dtype=torch.float16, # Sets the tensor type to float16 for faster computation
    device_map="auto", # Automatically maps the model layers to the available devices
    trust_remote_code=True, # Allows the execution of remote code for custom model configurations
    #attn_implementation="flash_attention_2", # Uses a specific attention implementation optimized for performance
    quantization_config=bnb_config, # Applies the BitsAndBytes configuration
)


#### Mistral Ends ####


# root for the script

root_dir = "miner_github/analyzer"

data_threshold = 5
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
def get_prediction_mistral(sample_commit_message):
    prompt_template = ''' <s> [INST] You are an analytical tool specialized in processing and classifying GitHub Commit message. Your task is to assess developer's intent in a given commit message and categorize it into one of the following predefined categories based on its content:
                      
                      'Yes':  A commit messages that explicitly mentions performance improvement or optimization, specifically in terms of execution time or resource utilization. The message should clearly indicate actions that made the code runs faster or  more efficiently, use less memory, or more efficiently utilize system resources. Also, if a commit message describes a change made to address a performance bottleneck, prevent performance degradation, reduce overheads or solve a problem that negatively affects performance. This includes optimizations like replacing inefficient code patterns that are known to kill performance even if the message does not use the words 'improvement' or 'performance' explicitly.
                      'No': A commit message that do not pertain to performance enhancements. This includes messages related to code changes for testing, documentation, performance profiling/monitoring/debugging/analysis and bug/error/crash fixes that don't explicitly mention performance improvement of the application itself, code refactoring or feature addition without explicit performance optimization,  and mentions of necessary or speculative or potential performance enhancements without concrete evidence or results. Also, a messages that is irrelevant, unclear, or ambiguous, and those that do not provide enough context to determine their intent.     

                    If the commit message doesn't fit clearly into any of the above categories, classify it as: 'No'. Additionally, pay close attention to the context in which terms like 'performance', 'improve' or 'improvements' are used. Not all improvements are related to performance—only, classify a message as 'Yes' if it specifically mentions enhancements related to execution time, memory usage, or resource efficiency. Avoid making assumptions based on ambiguous terms. You should have high confidence in classifying a message as 'Yes' based on careful examination of the information provided in the commit message.
                    If you encounter a commit message with multiple intentions, where at least one of those intentions includes a performance improvement, classify the entire message as 'Yes'.
                    You will only respond with the predefined category. Do not include the word 'Category'. Do not provide explanations or notes.
                    
                    Commit message : ```{commit_message}``` [/INST] Model_answer:  </s> '''
    generated_prompt = prompt_template.format(commit_message=sample_commit_message)
    inputs = tokenizer.apply_chat_template(
        [{'role': 'user', 'content': generated_prompt}],
        return_tensors="pt"
    ).to(model.device)
    outputs = model.generate(inputs, max_new_tokens=5, do_sample=True)
    return parse_output(tokenizer.decode(outputs[0], skip_special_tokens=True))


# def get_prediction(input_text):
#     """
#     Accepts input_text and predicts 3 classes: LABEL_0, LABEL_1(Perf) or LABEL_2 
#     """
    
#     # Tokenize the input text
#     inputs = tokenizer(input_text, return_tensors="pt",truncation=True, max_length=512)
#     # Move the input tensors to the same device as the model
#     inputs = {k: v.to(device) for k, v in inputs.items()}
#     with torch.no_grad():
#         logits = model(**inputs).logits
    
   
#     predicted_class_id = logits.argmax().item()
#     predicted_label = model.config.id2label[predicted_class_id]
#     return predicted_label


def get_ip_from_sshosts(sshosts_path):
    try:
        # Get the current node's hostname
        #hostname = socket.gethostname()
        with open(sshosts_path, 'r') as file:
            for line in file:
                line_hostname, ip_address = line.strip().split()
                if line_hostname == hostname:
                    return ip_address
    except Exception as e:
        logging.error(f"Error reading from sshosts: {e}")
        return None

def is_fork(repo_url):
    # Extract the repository's owner and name from the URL
    parts = repo_url.split('/')
    if len(parts) < 2:
        return None
    owner, repo_name = parts[-2], parts[-1]

    # GitHub API endpoint for getting repo details
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}"

    # Make a request to the GitHub API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        repo_data = response.json()
        return repo_data.get('fork', False)
    else:
        logging.info(f"Failed to fetch repository data: Status code {response.status_code}")
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



## object store code ##

def get_oci_config():
    """
    Load the OCI configuration. Modify this function if you need to load a specific profile.
    """
    return oci.config.from_file()


oci_config = get_oci_config()  # Load the OCI configuration

def upload_file_to_object_storage(namespace, bucket_name, object_name, file_path, oci_config):
    """
    Uploads a file to Oracle Cloud Infrastructure Object Storage using streaming and deletes the file afterwards.
    """
    object_storage_client = ObjectStorageClient(oci_config)
    with open(file_path, 'rb') as file: #rb for binary?
        object_storage_client.put_object(namespace, bucket_name, object_name, file)
        logging.info(f"Data upload completed: {object_name}")
    
    # Remove the file after successful upload
    try:
        os.remove(file_path)
        #print(f"Successfully deleted local file: {file_path}")
    except OSError as e:
        logging.info(f"Error deleting file {file_path}: {e}")

def write_commit_data_to_file_and_upload(namespace, bucket_name, commit_data, results_dir, batch_id):
    """
    Writes commit data to a .jsonl file, uploads it to OCI Object Storage, and removes the file locally.
    """
    #hostname = socket.gethostname()
    filename = f"{hostname}_batch_{batch_id}.jsonl"
    file_path = os.path.join(results_dir, filename)
    
    try:
        with open(file_path, 'w') as file:
            for commit_info in commit_data:
                file.write(json.dumps(commit_info) + '\n')
        
        #oci_config = get_oci_config()  # Load the OCI configuration
        upload_file_to_object_storage(namespace, bucket_name, filename, file_path, oci_config)
    except IOError as e:
        logging.info(f"An error occurred while writing or uploading the file: {e}")
    finally:
        commit_data.clear()


## object store code ends #$



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
                if len(commit_message.split()) <= 6:
                    continue
                if len(commit.modified_files) == 1 and get_prediction_mistral(commit_message).replace('\n','').strip() == "Yes": #get_prediction(commit_message) == 'LABEL_1':
                    modified_file = commit.modified_files[0]

                    if modified_file.change_type not in ["ADD", "DELETE"]:
                        if len(modified_file.changed_methods) == 1:
                            if 'merge' in commit_message or 'revert' in commit_message:
                                logging.info(f"Skipping merge commit: {commit.hash}")
                                continue
                            # get commit hash

                            # original source code
                            code_diff = modified_file.diff
                            src_original = modified_file.source_code_before or "na"
                            src_modified = modified_file.source_code or "na"
                            key = src_original + src_modified # the idea is comes from disticnt traning data sicne we pass this code, so focus on it
                            #deduplicate based on this

                            key_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
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
                                     func_token = func.token_count
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
                                'src_after': src_modified,
                                'diff': code_diff,
                                'func_no_tokens': func_token
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
                                #write_commit_data_to_file()
                                write_commit_data_to_file_and_upload(namespace, bucket_name, commit_data, results_dir, batch_id)
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
        if is_fork(repo_url) == True:
            continue
        repo_counter += 1
        logging.info(f"[{repo_counter}/{total_repo}]Processing reopository: {repo_url}")
        try:
            #analyze_repository(repo_url, output_csv_file_patterns1)
            mine_repo_commits(repo_url)
        except Exception as e:
            logging.error(f"Error processing this repository, continueing {repo_url}: {e}")
            continue
        # if total_found > MAX_COMMIT:
        #     logging.info("Exiting analysis!")
        #     break
        

    logging.info(f"Writing remaining commit data if any")
    #remaining data if any
    if commit_data:
        logging.info(f"Found remaining {len(commit_data)} commit rows")
        batch_id += 1
        #write_commit_data_to_file()
        write_commit_data_to_file_and_upload(namespace, bucket_name, commit_data, results_dir, batch_id)
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
