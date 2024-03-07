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
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Download the necessary NLTK models (run once)
nltk.download('punkt')

MAX_COMMIT = 2
# Disable tokenizers parallelism
os.environ["TOKENIZERS_PARALLELISM"] = "false"
cpu_count = os.cpu_count()-2
# Load the tokenizer and model only once
tokenizer = AutoTokenizer.from_pretrained("ManojAlexender/Finetuned_Final_LM_200k_v3")
model = AutoModelForSequenceClassification.from_pretrained("ManojAlexender/Finetuned_Final_LM_200k_v3")

 # Check if GPU (CUDA) is available, else use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# Move model to the chosen device
model.to(device)

# root for the script
root_dir = "miner_github/analyzer"
published_commits_patterns1 = 0
published_commits_patterns2 = 0
commit_counter_patterns1 = 0
commit_counter_patterns2 = 0
buffer_size = 100  # Set the number of commits after which the result file will be pushed to GitHub

# Logging configuration
logs_dir = os.path.join(root_dir, "logs") #log directory
os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists
log_file_path = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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



def count_tokens_code(code):
    tokens = nltk.word_tokenize(code)
    # Filter or process tokens as needed
    return len(tokens)

# function to get IP for the current host this script
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching public IP: {e}")
        return "ErrorFetchingIP"

# Create a 'results' directory if it doesn't exist
results_dir = f'{root_dir}/results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

def read_repository_urls_from_csv(input_csv_file):
    logging.info(f"Processing input filename: {input_csv_file}")
    with open(input_csv_file, 'r') as input_file:
        reader = csv.reader(input_file)
        next(reader, None)  # Skip the header row
        repo_urls = [row[6] for row in reader]
    return repo_urls

# dummy test function
def search_patterns_in_commit_message(message):
    if 'perf' in message:
        return True
    return False

def process_commit(commit, repo_url, commit_data, processed_commits, buffer_size, output_csv_file, commit_counter, published_commits):
    """
    Input: takes an 'commit' object and process it
    """
    try:

        logging.info(f"Processing commit: {commit.hash}: {commit.msg}")
        # get the commmit url
        commit_url = f"{repo_url}/commit/{commit.hash}"
        modified_file = commit.modified_files[0] # get the modified file
        if modified_file.change_type != "ADD" and modified_file.change_type != "DELETE":
            # first get all the methods in this modified file
            methods = modified_file.methods_before
            loc = ""
            changed_method_name = ""
            nlines = 0
            complexity = 0
            no_token = 0
            if len(modified_file.changed_methods) == 1:
                commit_message = commit.msg
                changed_method = modified_file.changed_methods[0]
                #extract info about this changed method
                method_name = changed_method.name # get the name of the changed method
                start_line = changed_method.start_line # its body start
                end_line = changed_method.end_line      # body end


                # now we need its original body, iterate over all original method and extract 
                for m in methods: 
                    if m == changed_method:
                        #print("FOUND")
                        pre_m_start = m.start_line # original method code
                        pre_m_end = m.end_line     # original method code ends
                        # print(m.start_line)
                        # print(m.end_line)

                # Extract method body from BEFORE change
                if modified_file.source_code_before:
                    lines_before = modified_file.source_code_before.split('\n')
                    #lines_before = modified_file.source_code_before
                    method_body_before = '\n'.join(lines_before[pre_m_start-1:pre_m_end])
                    #print(f"Method {method_name} BEFORE change:\n{method_body_before}\n")
                    
                # Extract method body from AFTER change
                if modified_file.source_code:
                    lines_after = modified_file.source_code.split('\n')
                    #lines_after = modified_file.source_code
                    method_body_after = '\n'.join(lines_after[start_line-1:end_line])

                # changed_method_name = ""
                # nlines = modified_file.nloc
                # complexity = modified_file.complexity
                # no_token = modified_file.token_count
                # diff_parsed_dict = modified_file.diff_parsed
                # diff_parsed_json = json.dumps(diff_parsed_dict)

                # changed_method_name = modified_file.changed_methods[0].name or "NA"
                # loc = "[" + str(modified_file.changed_methods[0].start_line) + ":"+ str(modified_file.changed_methods[0].end_line) + "]"
                # commit_data.append([commit.project_name, commit_url, commit.insertions, commit.deletions, commit.lines, commit.files])
                    
                #to get only commit messages uncomment 
                #commit_data.append([commit.project_name, commit_url, '"'+ commit.msg + '"',changed_method_name, loc])
                commit_data.append([commit.project_name, commit_url, '"'+ commit_message+ '"', method_name, method_body_before, method_body_after, count_tokens_code(commit_message), count_tokens_code(method_body_after)])

                #to get all uncomment
                #commit_data.append([commit.project_name, commit_url, commit.msg , src_before, src_current,diff_parsed_json, changed_method_name, loc, nlines,complexity,no_token])
                processed_commits.add(commit.hash)
                commit_counter += 1
        
        if commit_counter % buffer_size == 0:
            published_commits += buffer_size
            #write_commit_analysis_to_csv(output_csv_file, commit_data)
            write_commit_analysis_to_jsonl(output_csv_file, commit_data)
            logging.info(f"{commit_counter} commits processed and added to {output_csv_file}")
    except Exception as e:
        logging.error(f"Error processing commit {commit.hash}: {e}")
        # Decide on further actions: skip, retry, mark as processed, etc.    
    return commit_counter


def analyze_repository(repo_url, output_csv_file_pattern1):
    """
    repo_url: url for the repo to be analyzed, it analyzes all commit of this repo
    patterns: now we don't need it.
    """
    global commit_counter_patterns1, commit_counter_patterns2, published_commits_patterns1, published_commits_patterns2
    processed_commits = set()
    commit_data_patterns1 = []
    commit_data_patterns2 = []
    try:
        #provide number of worker threads to max capacity to reduce processing time
        for commit in Repository(repo_url, num_workers=cpu_count, only_modifications_with_file_types=['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cxx', '.c++']).traverse_commits():
            try:
                if commit.hash in processed_commits:
                    continue  # Skip already processed commits
                modified_files_count = len(commit.modified_files)
                if modified_files_count > 1: 
                    continue
                if modified_files_count == 1 and get_prediction(commit.msg) == 'LABEL_1':
                    commit_counter_patterns1 = process_commit(commit, repo_url, commit_data_patterns1, processed_commits, buffer_size, output_csv_file_pattern1, commit_counter_patterns1, published_commits_patterns1)
                # if modified_files_count < 10 and search_patterns_in_commit_message(commit.msg):
                #     commit_counter_patterns1 = process_commit(commit, repo_url, commit_data_patterns1, processed_commits, buffer_size, output_csv_file_pattern1, commit_counter_patterns1, published_commits_patterns1)        
                # fif patterns2 and modified_files_count < 10 and search_patterns_in_commit_message(commit.msg, patterns2):
                #     commit_counter_patterns2 = process_commit(commit, repo_url, commit_data_patterns2, processed_commits, buffer_size, output_csv_file_pattern2, commit_counter_patterns2, published_commits_patterns2)
            except Exception as e:
                logging.error(f"Failed to process commit {commit.hash} in repository {repo_url}: {e}")
                continue  # This will skip the rest of the current loop iteration and proceed to the next commit
            
            if commit_counter_patterns1 > MAX_COMMIT:
                logging.info("Desired number of commit found")
                break
    except Exception as e:
        logging.error(f"Failed to process repository {repo_url}: {e}")
    if commit_counter_patterns1 > published_commits_patterns1:
        #write_commit_analysis_to_csv(output_csv_file_pattern1, commit_data_patterns1)
        write_commit_analysis_to_jsonl(output_csv_file_pattern1, commit_data_patterns1)

    # if commit_counter_patterns2 > published_commits_patterns2:
    #     write_commit_analysis_to_csv(output_csv_file_pattern2, commit_data_patterns2)
    logging.info(f"Completed analysis for REPO: {repo_url}. Commits found: {commit_counter_patterns1}")

def write_commit_analysis_to_csv(output_csv_file, commit_data):
    with open(output_csv_file, 'a', newline='') as output_file:
        writer = csv.writer(output_file)
        if output_file.tell() == 0:
            # write all
            #writer.writerow(["project_name", "commit_url", "commit_message", "src_before", "src_after","diff_parsed", "changed_method_name", "loc", "m_nloc", "m_cc", "no_token"])

            # write commit message only
            #writer.writerow(["Project Name", "Commit URL", "Message", "changed_method_name", "loc"])
            writer.writerow(["project", "url", "commit_message", "modified_method", "method_src_before", "method_src_after", "msg_tokens", "src_tokens"])

        writer.writerows(commit_data)
    logging.info(f"Commit data written to {output_csv_file}")
    

# going to write data in .jsonl format becuse csv was breaking code data
def write_commit_analysis_to_jsonl(output_jsonl_file, commit_data):

    # Define a safe file size limit (e.g., 1 GB in this example)
    safe_file_size_limit = 7 * 1024 * 1024 * 1024  # 1 GB in bytes

    # Check the current file size
    if os.path.exists(output_jsonl_file):
        if os.path.getsize(output_jsonl_file) + len(json.dumps(commit_data)) > safe_file_size_limit:
            logging.error("Adding this commit would exceed the safe file size limit. Consider splitting the output into multiple files.")
            return

    try:
        #writer.writerow(["project", "url", "commit_message", "modified_method", "method_src_before", "method_src_after", "msg_tokens", "src_tokens"])
        with open(output_jsonl_file, 'a') as output_file:
            for record in commit_data:
                # Create a dictionary from the record data
                data = {
                    "project_name": record[0],
                    "commit_url": record[1],
                    "commit_message": record[2], # Remove extra quotes
                    "modified_method": record[3],
                    "method_src_before": record[4],
                    "method_src_after": record[5],
                    "msg_tokens": record[6],
                    "src_tokens": record[7]
                }
                # Write the JSON object to the file with a newline to separate records
                output_file.write(json.dumps(data) + '\n')
        logging.info(f"Commit data written to {output_jsonl_file}")
    except Exception as e:
        logging.error(f"Failed to write data to {output_jsonl_file}: {e}")

def main():
    global commit_counter_patterns1
    logging.info("Script started")
    host_ip = get_public_ip()
    date = datetime.date.today().strftime("%m%d%Y")
    input_csv_file = os.path.join(root_dir, f"github_repositories_{host_ip}.csv")
    
    repo_urls = read_repository_urls_from_csv(input_csv_file)
    output_csv_file_patterns1 = os.path.join(results_dir, f"github_repo_analysis_result_{date}_{host_ip}_perf.jsonl")
    # patterns1 = ['perf', 'performance']
    # output_csv_file_patterns2 = os.path.join(results_dir, f"github_repo_analysis_result_{date}_{host_ip}_p2.csv")
    # patterns2 = ['mem', 'memory']

    for repo_url in repo_urls:
        logging.info(f"Processing repo URL: {repo_url}")
        analyze_repository(repo_url, output_csv_file_patterns1)
        if commit_counter_patterns1 > MAX_COMMIT:
            logging.info("Exiting analysis!")
            break
    logging.info(f"Analysis is complete! Creating poll text file..")
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
