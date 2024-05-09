import socket
from pydriller import Repository
import pandas as pd
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
import gc
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
bucket_name = 'bucket-lang-c-ds'


MAX_COMMIT = 100000  #define max number of commits to be collected, uncomment if not necessary

# Initialize a global batch_id
batch_id = 0
batch_id_url = 0
seen_hashes = set()
total_found = 0
total_found_url = 0
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
##### Roberta ########
# Load the tokenizer and model only once

tokenizer = AutoTokenizer.from_pretrained("ManojAlexender/final_roberta_with_new_400k_plus_37k_Best")
model = AutoModelForSequenceClassification.from_pretrained("ManojAlexender/final_roberta_with_new_400k_plus_37k_Best")
# Move model to the chosen device
model.to(device)

# #### Roberta Ends #####

# #### Mistral #####
# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True, # Enables loading the model in 4-bit precision
#     bnb_4bit_quant_type="nf4", # Specifies the quantization type
#     bnb_4bit_use_double_quant=True, # Enables double quantization for better precision
# )
# # Loading the tokenizer
# tokenizer = AutoTokenizer.from_pretrained("/home/ubuntu/Mistral-7B-Instruct-v0.2")
# # Loading the model with BitsAndBytes configuration, and additional settings from Method-1
# model = AutoModelForCausalLM.from_pretrained(
#     "/home/ubuntu/Mistral-7B-Instruct-v0.2",
#     torch_dtype=torch.float16, # Sets the tensor type to float16 for faster computation
#     device_map="auto", # Automatically maps the model layers to the available devices
#     trust_remote_code=True, # Allows the execution of remote code for custom model configurations
#     #attn_implementation="flash_attention_2", # Uses a specific attention implementation optimized for performance
#     quantization_config=bnb_config, # Applies the BitsAndBytes configuration
# )


#### Mistral Ends ####


# root for the script

root_dir = "miner_github/analyzer"

data_threshold = 250
commit_data = [] # running commit buffer
commit_data_url = []

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

# prompt_template = ''' <s> [INST] You are an analytical tool specialized in processing and classifying GitHub Commit message. Your task is to assess developer's intent in a given commit message and categorize it into one of the following predefined categories based on its content:
                    
#                     'Yes':  A commit messages that explicitly mentions performance improvement or optimization, specifically in terms of execution time or resource utilization or trade-off between the two. The message should clearly indicate actions that made the code runs faster or  more efficiently, use less memory, or more efficiently utilize system resources. Also, if a commit message describes a change made to address a performance bottleneck, prevent performance degradation, reduce overheads or solve a problem that negatively affects performance. This includes optimizations like replacing inefficient code patterns that are known to kill performance even if the message does not use the words 'improvement' or 'performance' explicitly.
#                     'No': A commit message that do not pertain to performance enhancements. This includes messages related to code changes for testing, documentation, performance profiling/monitoring/debugging/analysis and bug/error/crash fixes that don't explicitly mention performance improvement of the application itself, code refactoring or feature addition without explicit performance optimization,  and mentions of necessary or speculative or potential performance enhancements without concrete evidence or results. Also, a messages that is irrelevant, unclear, or ambiguous, and those that do not provide enough context to determine their intent.     

#                 If the commit message doesn't fit clearly into any of the above categories, classify it as: 'No'. Additionally, pay close attention to the context in which terms like 'performance', 'improve' or 'improvements' are used. Not all improvements are related to performance—only, classify a message as 'Yes' if it specifically mentions enhancements related to execution time, memory usage, or resource efficiency. Avoid making assumptions based on ambiguous terms. You should have high confidence in classifying a message as 'Yes' based on careful examination of the information provided in the commit message.
#                 If you encounter a commit message with multiple intentions, where at least one of those intentions includes a performance improvement, classify the entire message as 'Yes'.
#                 You will only respond with the predefined category. Do not include the word 'Category'. Do not provide explanations or notes.
                
#                 Commit message : ```{commit_message}``` [/INST] Model answer:  </s> '''

# use the loaded model to predict classificaiton
# def get_prediction_mistral(sample_commit_message):
#     generated_prompt = prompt_template.format(commit_message=sample_commit_message)
#     inputs = tokenizer.apply_chat_template(
#         [{'role': 'user', 'content': generated_prompt}],
#         return_tensors="pt",
#         truncation=True,
#         max_length =4097 
#     ).to(model.device)
#     outputs = model.generate(inputs, max_new_tokens=5, do_sample=False) # for deterministic output
#     value = parse_output(tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True))
#     if value == 'Yes':
#         return True
#     else:
#         return False


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
    return predicted_label == 'LABEL_1'


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


def get_info(repo_url):
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
        # return repo_data.get('fork', False)
        fork = repo_data.get('fork', False)
        size = repo_data.get('size', 0)
        return { "fork": fork, "size": size}
    else:
        logging.info(f"Failed to fetch repository data: Status code {response.status_code}")
        return None

def get_public_ip(sshhosts_path='/home/ubuntu/miner_github/sshhosts_hostname'):
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
12
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

    try:
        with open(file_path, 'rb') as file:
            object_storage_client.put_object(namespace, bucket_name, object_name, file)
            logging.info(f"Data upload completed: {object_name}")
            os.remove(file_path)  # Remove the file after successful upload
            logging.info(f"Successfully deleted local file: {file_path}")
    except Exception as e:  # Catch any exception during upload or file handling
        logging.error(f"Failed to upload file {file_path} due to: {e}")


def write_commit_data_to_file_and_upload(namespace, bucket_name, results_dir):
    """
    Writes commit data to a .jsonl file, uploads it to OCI Object Storage, and removes the file locally.
    """
    global commit_data
    global batch_id
    #hostname = socket.gethostname()
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time to include year, month, day, hour, minute, and second
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"CPerf_{hostname}_batch_{batch_id}_{timestamp}.jsonl"
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
        logging.info(f"PERF{batch_id}: uploading complete!")
        # garbage collect and emtpy cache
        torch.cuda.empty_cache()
        gc.collect()

# for nonperf commit data write
def write_commit_data_to_file_and_upload_url(namespace, bucket_name, results_dir):
    """
    Writes commit data to a .jsonl file, uploads it to OCI Object Storage, and removes the file locally.
    """
    global commit_data_url
    global batch_id_url

    #hostname = socket.gethostname()
       # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time to include year, month, day, hour, minute, and second
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"CPerfURL_{hostname}_batch_{batch_id_url}_{timestamp}.jsonl"
    file_path = os.path.join(results_dir, filename)
    
    try:
        with open(file_path, 'w') as file:
            for commit_info in commit_data_url:
                file.write(json.dumps(commit_info) + '\n')
        
        #oci_config = get_oci_config()  # Load the OCI configuration
        upload_file_to_object_storage(namespace, bucket_name, filename, file_path, oci_config)
    except IOError as e:
        logging.info(f"An error occurred while writing or uploading the file: {e}")
    finally:
        commit_data_url.clear()
        logging.info(f"CPerf>20: uploading complete!")


## object store code ends #$

# regex to clean commit message

fixes_re = re.compile("fix(es)?\\s+#\\d+", re.I)
merge_re0 = re.compile("merge pull request[^\\n]+", re.I)
merge_re1 = re.compile("Merge (remote-tracking )?branch[^\\n]+", re.I)
sign_re0 = re.compile("(Signed-off-by|Reviewed-By|Change-Id):[^\\n]+", re.I)
git_svn_re0 = re.compile("git-svn-id:[^\\n]+", re.I)
bot_re0 = re.compile("(.|\n)*dependabot(.|\n)*", re.I)
ticket_re0 = re.compile("Ticket: [^\\n]+", re.I)

# python ['.py']
# c/c++ ['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx']

def mine_repo_commits(repo_url, file_types=['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx']):
    global seen_hashes
    global batch_id
    global batch_id_url
    global total_found
    global total_found_url
    global commit_data
    global commit_data_url
    global data_threshold
    global repo_counter_fail
    global repo_counter_success
    local_commit_counter = 0
    local_commit_counter_url = 0
    start_time = time.time()  # Record the start time for the current repository

    try:
        for commit in Repository(repo_url, only_no_merge=True, only_modifications_with_file_types=file_types).traverse_commits():
            try: 
                commit_message = commit.msg
                # clean data please
                commit_message = fixes_re.sub("", commit_message)
                commit_message = merge_re0.sub("", commit_message)
                commit_message = merge_re1.sub("", commit_message)
                commit_message = sign_re0.sub("", commit_message)
                commit_message = git_svn_re0.sub("", commit_message)
                commit_message = bot_re0.sub("", commit_message)
                commit_message = bot_re0.sub("", commit_message)
                commit_message = ticket_re0.sub("", commit_message)
                commit_message = commit_message.replace('\n', ' ').strip()
                
                l = len(commit_message.split())
                logging.info(f"commit_message_length:[{l}]")
                if l <= 6:
                    continue
                no_changed_files = commit.files
                if  no_changed_files == 1: # and get_prediction_mistral(commit_message): #get_prediction(commit_message) == 'LABEL_1':
                    modified_file = commit.modified_files[0]

                    if modified_file.change_type not in ["ADD", "DELETE"]:
                        no_modified_method = len(modified_file.changed_methods)
                        if  no_modified_method == 1:
                            pred = get_prediction(commit_message)
                            if pred == True:
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
                                #file_tokens = modified_file.token_count
                                n_loc = modified_file.nloc
                                n_added_lines = modified_file.added_lines
                                n_deleted_lines = modified_file.deleted_lines
                                
                                author = commit.author
                                # its time to concat all these info
                                commit_info = {
                                    'project_name': commit.project_name,
                                    'commit_url': commit_url + '/commit/' + commit.hash,
                                    'commit_message': commit_message,
                                    'filename': filename,
                                    'commit_date': str(commit.committer_date),
                                    'author_email': author.email,
                                    'author_name': author.name,
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
                                logging.info(f"Total perf found: {total_found}")

                                if len(commit_data) == data_threshold:
                                    batch_id += 1
                                    #write_commit_data_to_file()
                                    write_commit_data_to_file_and_upload(namespace, bucket_name, results_dir)
                            # else:
                            #     if 'merge' in commit_message or 'revert' in commit_message:
                            #         logging.info(f"Skipping merge commit: {commit.hash}")
                            #         continue
                            #     # get commit hash

                            #     # original source code
                            #     code_diff = modified_file.diff
                            #     src_original = modified_file.source_code_before or "na"
                            #     src_modified = modified_file.source_code or "na"
                            #     key = src_original + src_modified # the idea is comes from disticnt traning data sicne we pass this code, so focus on it
                            #     #deduplicate based on this

                            #     key_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
                            #     if key_hash in seen_hashes:
                            #         logging.info(f"Skipping duplicate commit: {commit.hash}")
                            #         continue
                            #     #now proceed, extract info for this commit which met all our critera
                            #     # get changed method name
                            #     changed_method_name = modified_file.changed_methods[0].name
                                
                            #     # get the commmit url
                            #     commit_url = repo_url
                            #     # get hash 
                            #     sha = commit.hash
                            #     # get filename
                            #     filename = modified_file.filename
                            #     # get changed method's location
                            #     changed_method_loc_start = modified_file.changed_methods[0].start_line
                            #     changed_method_loc_end = modified_file.changed_methods[0].end_line
                            #     loc_changed_method = f'[{changed_method_loc_start}:{changed_method_loc_end}]'
                            #     # get the list of methods in this file
                            #     methods = modified_file.methods_before
                            #     # now iterate through these methods to extract original version
                            #     # of the changed_method
                            #     for func in methods:
                            #         if func.name == changed_method_name:
                            #             orig_method_loc_start = func.start_line
                            #             orig_method_loc_end = func.end_line
                            #             func_token = func.token_count
                            #             break
                            #     loc_orig_method = f'[{orig_method_loc_start}:{orig_method_loc_end}]'
                                
                            #     #get tokens in file
                            #     #file_tokens = modified_file.token_count
                            #     n_loc = modified_file.nloc
                            #     n_added_lines = modified_file.added_lines
                            #     n_deleted_lines = modified_file.deleted_lines
                                
                            #     # its time to concat all these info
                            #     commit_info = {
                            #         'commit_url': commit_url + '/commit/' + commit.hash,
                            #         'commit_message': commit_message,
                            #         'filename': filename,
                            #         'commit_date': str(commit.committer_date),
                            #         #'no_tokens': file_tokens,
                            #         'nloc': n_loc,
                            #         'n_added_lines': n_added_lines,
                            #         'n_deleted_lines': n_deleted_lines,
                            #         'modified_method': changed_method_name,
                            #         'loc_before': loc_orig_method,
                            #         'loc_after': loc_changed_method,
                            #         'src_before': src_original,
                            #         'src_after': src_modified,
                            #         'diff': code_diff,
                            #         'func_no_tokens': func_token
                            #     }
                            #     # add this commit info to running list
                            #     commit_data_nperf.append(commit_info)
                            #     # mark it seen to avoid duplicate
                            #     seen_hashes.add(key_hash)
                            #     total_found_nperf += 1
                            #     local_commit_counter_nperf += 1
                            #     logging.info(f"Total nperf found: {total_found_nperf}")

                            #     if len(commit_data_nperf) == data_threshold:
                            #         batch_id_nperf += 1
                            #         #write_commit_data_to_file()
                            #         write_commit_data_to_file_and_upload_nperf(namespace, bucket_name, results_dir)
                elif no_changed_files> 1 and no_changed_files <= 20 and get_prediction(commit_message):
                    commit_info = {
                        'url': repo_url + '/commit/' + commit.hash
                    }
                    # add this commit info to running list
                    commit_data_url.append(commit_info)
                    if len(commit_data_url) == data_threshold:
                        batch_id_url += 1
                        #write_commit_data_to_file()
                        write_commit_data_to_file_and_upload_url(namespace, bucket_name, results_dir)
        
                    
                
            except Exception as commit_error:
                logging.error(f"Error processing commit '{commit.hash}' in repository '{repo_url}': {commit_error}")
                # Continue to the next commit despite the error
                continue
        repo_counter_success += 1
        return True
    except Exception as repo_error:
        repo_counter_fail += 1
        logging.error(f"Error while accessing repository '{repo_url}': {repo_error}")
        return False
        
        # Continue to the next repository despite the error

    finally:
        end_time = time.time()  # End time for the current repository
        time_taken = end_time - start_time
        logging.info(f"Time taken for processing {repo_url}: {time_taken} seconds")
        logging.info(f"local_commit_found (perf/nperf):{local_commit_counter}/{local_commit_counter_url}: {repo_url}")



def main():
    global batch_id
    global batch_id_url
    global total_found
    global total_found_url
    global commit_data
    global commit_data_url
    global repo_counter_fail
    global repo_counter_success
    logging.info("Starting mining..")

    host_ip = get_public_ip()
    date = datetime.date.today().strftime("%m%d%Y")
    
    # here we read the .csv file containg this node's split of the repo list to be mined
    input_csv_file = os.path.join(root_dir, f"github_repositories_{host_ip}.csv")
    # create df frame
    df = pd.read_csv(input_csv_file)
    logging.info(f"CSV loaded into df!")
    repo_urls = read_repository_urls_from_csv(input_csv_file)
    unique_repo_urls = list(set(repo_urls))
    #repo_urls = ['https://github.com/opencv/opencv']  # List of repository URLs to process

    # process all the repositories in the list
    repo_counter = 0

    total_repo = len(unique_repo_urls)
    
    if 'processed' not in df.columns:
        df['processed'] = False
        logging.info(f"processed columnd added to csv")
    df.to_csv(input_csv_file, index=False)
    logging.info(f"CSV file updated!")


    time_start = time.time()
    #for repo_url in unique_repo_urls:
    for index, row in df.iterrows():
        repo_url = row['url']

        if row['processed']:
            logging.info(f"Skipping already processed repo: {repo_url}")
            #batch_id = batch_id_nperf = 1000000
            continue
        #get meta data size is_fork
        
        try:
            meta_data = get_info(repo_url)
            if meta_data is not None:
                logging.info(f"Successfully retrieved metadata:{meta_data}")
                # You can access the dictionary as expected
                fork_status = meta_data["fork"]
                repo_size = meta_data["size"]
                #print(f"Fork: {fork_status}, Size: {repo_size} kB")
                if fork_status == True:
                    logging.info(f"Forked skipping")
                    continue
                if int(repo_size) > 2e6:
                    logging.info(f"LargeFile! Skipping")
                    continue
            else:
                # Handle the case where no data was returned
                logging.info(f"No metadata could be retrieved.")
        except Exception as e:
            logging.info(f"An error occurred while fetching the metadata: {e}")
        #meta_data = get_info(repo_url)
        repo_counter += 1
        logging.info(f"[{repo_counter}/{total_repo}]Processing reopository: {repo_url}")
        
        # call miner function
        result = mine_repo_commits(repo_url) 

        df.at[index, 'processed'] = result
        df.to_csv(input_csv_file,index=False)
        logging.info(f"Updated csv file with current repo status!")

        if not result:
            logging.info(f"Failed to process repo: {repo_url}")


        # if total_found > MAX_COMMIT:
        #     logging.info("Exiting analysis!")
        #     break
        

    logging.info(f"Writing remaining commit data if any")
    #remaining data if any
    if commit_data:
        logging.info(f"Found remaining {len(commit_data)} commit rows")
        batch_id += 1
        #write_commit_data_to_file()
        write_commit_data_to_file_and_upload(namespace, bucket_name,results_dir)
        #remaining data if any
    if commit_data_url:
        logging.info(f"Found remaining {len(commit_data_url)} commit rows")
        batch_id_url += 1
        #write_commit_data_to_file()
        write_commit_data_to_file_and_upload_url(namespace, bucket_name, results_dir)
    time_finish = time.time()
    total_time = time_finish - time_start
    minutes, seconds = divmod(total_time, 60)
    logging.info(f"Analysis is complete!. Creating poll text file..")
    
    # record summary
    logging.info(f"Total repository: {total_repo}")
    logging.info(f"Total successfully processed: {repo_counter_success}")
    logging.info(f"Total failed to process: {repo_counter_fail}")
    logging.info(f"Total perf commit curated: {total_found}")
    logging.info(f"Total >20 changedFile commit curated: {total_found_url}")
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
