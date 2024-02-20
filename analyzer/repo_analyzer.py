import socket
from pydriller import Repository
import csv
import os
import datetime
import requests
import logging
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Disable tokenizers parallelism
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Load the tokenizer and model only once
tokenizer = AutoTokenizer.from_pretrained("ManojAlexender/Finetuned_Final_LM_200k_v3")
model = AutoModelForSequenceClassification.from_pretrained("ManojAlexender/Finetuned_Final_LM_200k_v3")

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
    with torch.no_grad():
        logits = model(**inputs).logits
    
    predicted_class_id = logits.argmax().item()
    predicted_label = model.config.id2label[predicted_class_id]
    return predicted_label


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
    logging.info(f"Processing commit: {commit.hash}: {commit.msg}")
    # get the commmit url
    commit_url = f"{repo_url}/commit/{commit.hash}"
    modified_file = commit.modified_files[0]
    if modified_file.change_type != "ADD" and modified_file.change_type != "DELETE":
        src_before = modified_file.source_code_before or "NA"
        src_current = modified_file.source_code or "NA"
        changed_method_name = ""
        loc = ""
        if len(modified_file.changed_methods) == 1:
            changed_method_name = modified_file.changed_methods[0].name or "NA"
            loc = "[" + str(modified_file.changed_methods[0].start_line) + ":"+ str(modified_file.changed_methods[0].end_line) + "]"
        # commit_data.append([commit.project_name, commit_url, commit.insertions, commit.deletions, commit.lines, commit.files])
            
        #to get only commit messages uncomment 
        commit_data.append([commit.project_name, commit_url, '"'+ commit.msg + '"'])

        #to get all uncomment
        #commit_data.append([commit.project_name, commit_url, '"'+ commit.msg + '"', '"'+ src_before +'"', '"'+ src_current +'"', changed_method_name, loc])
        processed_commits.add(commit.hash)
        commit_counter += 1
    
    if commit_counter % buffer_size == 0:
        published_commits += buffer_size
        write_commit_analysis_to_csv(output_csv_file, commit_data)
        logging.info(f"{commit_counter} commits processed and added to {output_csv_file}")
    
    return commit_counter

def analyze_repository(repo_url, output_csv_file_pattern1):
    """
    repo_url: url for the repo to be analyzed
    patterns: now we don't need it.
    """
    global commit_counter_patterns1, commit_counter_patterns2, published_commits_patterns1, published_commits_patterns2
    processed_commits = set()
    commit_data_patterns1 = []
    commit_data_patterns2 = []
    for commit in Repository(repo_url, only_modifications_with_file_types=['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp']).traverse_commits():
        if commit.hash in processed_commits:
            continue  # Skip already processed commits
        modified_files_count = len(commit.modified_files)
        
        if modified_files_count == 1 and get_prediction(commit.msg) == 'LABEL_1':
            commit_counter_patterns1 = process_commit(commit, repo_url, commit_data_patterns1, processed_commits, buffer_size, output_csv_file_pattern1, commit_counter_patterns1, published_commits_patterns1)
        # if modified_files_count < 10 and search_patterns_in_commit_message(commit.msg):
        #     commit_counter_patterns1 = process_commit(commit, repo_url, commit_data_patterns1, processed_commits, buffer_size, output_csv_file_pattern1, commit_counter_patterns1, published_commits_patterns1)        
        # fif patterns2 and modified_files_count < 10 and search_patterns_in_commit_message(commit.msg, patterns2):
        #     commit_counter_patterns2 = process_commit(commit, repo_url, commit_data_patterns2, processed_commits, buffer_size, output_csv_file_pattern2, commit_counter_patterns2, published_commits_patterns2)
        if commit_counter_patterns1 > 3000:
            break
    if commit_counter_patterns1 > published_commits_patterns1:
        write_commit_analysis_to_csv(output_csv_file_pattern1, commit_data_patterns1)

    # if commit_counter_patterns2 > published_commits_patterns2:
    #     write_commit_analysis_to_csv(output_csv_file_pattern2, commit_data_patterns2)
    logging.info(f"Completed analysis for {repo_url}. Commits found: Pattern1={commit_counter_patterns1}")

def write_commit_analysis_to_csv(output_csv_file, commit_data):
    with open(output_csv_file, 'a', newline='') as output_file:
        writer = csv.writer(output_file)
        if output_file.tell() == 0:
            # write all
            #writer.writerow(["Project Name", "Commit URL", "Message", "src_before", "src", "changed_method_name", "loc"])

            # write commit message only
            writer.writerow(["Project Name", "Commit URL", "Message"])

        writer.writerows(commit_data)
    logging.info(f"Commit data written to {output_csv_file}")

def main():
    logging.info("Script started")
    host_ip = get_public_ip()
    date = datetime.date.today().strftime("%m%d%Y")
    input_csv_file = os.path.join(root_dir, f"github_repositories_{host_ip}.csv")
    
    repo_urls = read_repository_urls_from_csv(input_csv_file)
    output_csv_file_patterns1 = os.path.join(results_dir, f"github_repo_analysis_result_{date}_{host_ip}_perf.csv")
    # patterns1 = ['perf', 'performance']
    # output_csv_file_patterns2 = os.path.join(results_dir, f"github_repo_analysis_result_{date}_{host_ip}_p2.csv")
    # patterns2 = ['mem', 'memory']
    
    for repo_url in repo_urls:
        logging.info(f"Processing repo URL: {repo_url}")
        analyze_repository(repo_url, output_csv_file_patterns1)
        logging.info(f"Analysis is complete!")

if __name__ == "__main__":
    main()
