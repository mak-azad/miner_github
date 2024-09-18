import pandas as pd
from pydriller import Repository
import re
from collections import defaultdict
import logging
import os
import datetime
import json


# Logging configuration
root_dir = "./"
logs_dir = os.path.join(root_dir, "logs")  # log directory
os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists
log_file_path = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: Read the CSV file
csv_file_path = 'commits_short.csv'
df = pd.read_csv(csv_file_path)


def generate_commit_url(repo_url, commit_hash):
    # Remove the '.git' part from the repo URL, if present
    if repo_url.endswith('.git'):
        repo_url = repo_url[:-4]
    
    # Construct the commit URL
    commit_url = f"{repo_url}/commit/{commit_hash}"
    
    return commit_url

# Step 2: Extract repository URL and commit hash from each URL
def extract_repo_commit_info(url):
    match = re.match(r'https://github\.com/(.+)/commit/([a-f0-9]{40})', url)
    if match:
        repo_path = f"https://github.com/{match.group(1)}.git"
        commit_hash = match.group(2)
        return repo_path, commit_hash
    else:
        raise ValueError(f"Invalid URL format: {url}")

# Step 3: Group commits by repository URL
repo_commits = defaultdict(list)

for url in df['commit_url']:  # Assuming the CSV file has a column named 'url'
    try:
        repo_path, commit_hash = extract_repo_commit_info(url)
        repo_commits[repo_path].append(commit_hash)
    except ValueError as ve:
        print(ve)



# Step 4: Initialize a list to collect relevant commit data
filtered_commits = []

# JSONL file path
jsonl_file_path = 'filtered_commits.jsonl'

# Refactored Step 5: Process each repository and its commits with exception handling
def process_repo_commits(repo_commits):
    logging.info(f"Total repo to process: {len(repo_commits)}")
    #file_types = ['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx']  # for C/C++
    #only_modifications_with_file_types=file_types
    for repo_path, commits in repo_commits.items():  # Iterate over repositories and their commits
        try:
            logging.info(f"Analyzing repository: {repo_path}")
            logging.info(f"Total commits in this repo: {len(commits)}")
            cnt = 0
            for commit in Repository(repo_path, only_commits=commits).traverse_commits():
                cnt += 1
                try:
                    # Check for commits with exactly one function changed
                    if len(commit.modified_files) == 1:  # Ensure only one file was modified
                        modified_file = commit.modified_files[0]

                        # Check if the change type is not 'ADD' or 'DELETE'
                        if modified_file.change_type not in ["ADD", "DELETE"]:
                            no_modified_methods = len(modified_file.changed_methods)
                            
                            # Check if exactly one function was changed
                            if no_modified_methods == 1:
                                # Extract data
                                commit_message = commit.msg
                                commit_sha = commit.hash
                                commit_url = generate_commit_url(repo_path, commit_sha)
                                code_diff = modified_file.diff
                                #src_original = modified_file.source_code_before or "na"
                                #src_modified = modified_file.source_code or "na"
                                changed_method_name = modified_file.changed_methods[0].name
                    
                                # Create the commit data dictionary
                                commit_data = {
                                    'commit_url': commit_url,
                                    'commit_message': commit_message,
                                    'code_diff': code_diff,
                                    #'src_original': src_original,
                                    #'src_modified': src_modified,
                                    'changed_method_name': changed_method_name
                                }

                                # Write the commit data to the JSONL file
                                with open(jsonl_file_path, 'a') as jsonl_file:
                                    jsonl_file.write(json.dumps(commit_data) + '\n')  # Write JSON data in a new line
                                
                except Exception as e:
                    logging.error(f"Error processing commit {commit.hash} in {repo_path}: {str(e)}")
                    # Continue processing the next commit in case of error
                    continue
            logging.info(f" Total commit processed: {cnt}")
        except Exception as e:
            logging.error(f"Error processing repository {repo_path}: {str(e)}")
            # Continue with the next repository in case of error
            continue

# Step 6: Save the filtered commits to a CSV file (optional, you can keep this for other needs)
output_csv_path = 'filtered_commits.csv'

# Call the function to process the commits
process_repo_commits(repo_commits)

# Save filtered commits to a CSV (optional)
filtered_commits_df = pd.DataFrame(filtered_commits)
filtered_commits_df.to_csv(output_csv_path, index=False)

print(f"Filtered commits saved to {output_csv_path} and {jsonl_file_path}")





# import pandas as pd
# from pydriller import Repository
# import re
# from collections import defaultdict
# import logging
# import os
# import datetime


# # Logging configuration
# root_dir = "./"
# logs_dir = os.path.join(root_dir, "logs") #log directory
# os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists
# log_file_path = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
# logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Step 1: Read the CSV file
# csv_file_path = 'commits.csv'
# df = pd.read_csv(csv_file_path)


# def generate_commit_url(repo_url, commit_hash):
#     # Remove the '.git' part from the repo URL, if present
#     if repo_url.endswith('.git'):
#         repo_url = repo_url[:-4]
    
#     # Construct the commit URL
#     commit_url = f"{repo_url}/commit/{commit_hash}"
    
#     return commit_url

# # Step 2: Extract repository URL and commit hash from each URL
# def extract_repo_commit_info(url):
#     match = re.match(r'https://github\.com/(.+)/commit/([a-f0-9]{40})', url)
#     if match:
#         repo_path = f"https://github.com/{match.group(1)}.git"
#         commit_hash = match.group(2)
#         return repo_path, commit_hash
#     else:
#         raise ValueError(f"Invalid URL format: {url}")

# # Step 3: Group commits by repository URL
# repo_commits = defaultdict(list)

# for url in df['commit_url']:  # Assuming the CSV file has a column named 'url'
#     try:
#         repo_path, commit_hash = extract_repo_commit_info(url)
#         repo_commits[repo_path].append(commit_hash)
#     except ValueError as ve:
#         print(ve)

# # Step 4: Initialize a list to collect relevant commit data
# filtered_commits = []

# # Step 5: Process each repository and its commits
# file_types = ['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx'] # for c/c++
# for repo_path, commits in repo_commits.items(): # at this point we have repo urls and its commits
#     logging.info(f"Analyzing repository: {repo_path}")
    
    
#     # Use PyDriller to analyze each commit in the repository
#     for commit in Repository(repo_path, only_commits=commits, only_modifications_with_file_types= file_types).traverse_commits():
#         #print(f"Commit {commit.hash}: {commit.msg}")

#         # Check for commits with exactly one function changed
#         if len(commit.modified_files) == 1:  # Ensure only one file was modified
#             modified_file = commit.modified_files[0]

#             # Check if the change type is not 'ADD' or 'DELETE'
#             if modified_file.change_type not in ["ADD", "DELETE"]:
#                 no_modified_methods = len(modified_file.changed_methods)
                
#                 # Check if exactly one function was changed
#                 if no_modified_methods == 1:
#                     #extract data
#                     commit_message = commit.msg
#                     commit_sha = commit.hash
#                     commit_url = generate_commit_url(repo_path,commit_sha)
#                     # original source code
#                     code_diff = modified_file.diff
#                     src_original = modified_file.source_code_before or "na"
#                     src_modified = modified_file.source_code or "na"
#                     changed_method_name = modified_file.changed_methods[0].name
        
#                     # Collect the commit data
#                     filtered_commits.append({
#                         'commit_url': commit_url,
#                         'commit_message': commit.msg
#                     })

# # Step 6: Save the filtered commits to a CSV file
# output_csv_path = 'filtered_commits.csv'
# filtered_commits_df = pd.DataFrame(filtered_commits)
# filtered_commits_df.to_csv(output_csv_path, index=False)

# print(f"Filtered commits saved to {output_csv_path}")
