from pydriller import Repository
import logging
import datetime
import os
import time
import hashlib
import re

# Initialize a global batch_id
batch_id = 0
batch_id_url = 0
batch_id_dev = 0
seen_hashes = set()
total_found = 0
total_found_url = 0
repo_counter_success = 0
repo_counter_fail = 0


commit_data = [] # running commit buffer
commit_data_url = []
commit_dev_exp = []

root_dir = "/home/ubuntu"
# Logging configuration
logs_dir = os.path.join(root_dir, "logs") #log directory
os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists
log_file_path = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#file_types=['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx', '.py','.java', '.F']

# #414ddb54b2aea290f44fa5fd4108136beeab9d7a
# repo_url = 'https://github.com/trilinos/Trilinos'
# for commit in Repository(repo_url, only_no_merge=True, only_modifications_with_file_types=file_types).traverse_commits():
#     try: 
#         commit_message = commit.hash
                
#         print(commit_message.hash)
#     except Exception as commit_error:
#         print(f"Error processing commit '{commit.hash}' in repository '{repo_url}': {commit_error}")
#         # Continue to the next commit despite the error
#         continue

fixes_re = re.compile("fix(es)?\\s+#\\d+", re.I)
merge_re0 = re.compile("merge pull request[^\\n]+", re.I)
merge_re1 = re.compile("Merge (remote-tracking )?branch[^\\n]+", re.I)
sign_re0 = re.compile("(Signed-off-by|Reviewed-By|Change-Id):[^\\n]+", re.I)
git_svn_re0 = re.compile("git-svn-id:[^\\n]+", re.I)
bot_re0 = re.compile("(.|\n)*dependabot(.|\n)*", re.I)
ticket_re0 = re.compile("Ticket: [^\\n]+", re.I)
    
def mine_repo_commits(repo_url, file_types=['.cu', '.cuh', '.c', '.h', '.cpp', '.hpp', '.cc', '.c++', '.cxx', '.py','.java', '.F']):
    global seen_hashes
    global commit_dev_exp
    global batch_id
    global batch_id_url
    global batch_id_dev
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
        for commit in Repository(repo_url, only_no_merge=True, single='8217166492ca50cddd0725d029f46d19c274640c', only_modifications_with_file_types=file_types).traverse_commits():
            try: 
                commit_message = commit.msg
                l = len(commit_message.split())
                if l > 1000:
                    logging.info(f"Too big commit message!")
                    continue
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
                
  
                #logging.info(f"commit_message_length:[{l}]")
                if l <= 6:
                    continue
                
                commit_message = commit_message.lower()
                
                # apply ML model wheather this commit is related to performance or not
                pred = "0" #get_prediction(commit_message)
                
                #here we extract all the information common to perf/nonperf commit
                no_changed_files = commit.files
                if no_changed_files > 1:
                    logging.info(f"Skipping more than 1 file change! - {no_changed_files}")
                    continue
                modified_file = commit.modified_files[0]
                    
                commit_url = repo_url + '/commit/' + commit.hash
                commit_dev_email = commit.author.email
                commit_dev_name = commit.author.name
                n_added_lines = modified_file.added_lines
                n_deleted_lines = modified_file.deleted_lines
                # checking for deduplication
                code_diff = modified_file.diff
                src_original = modified_file.source_code_before or "na"
                src_modified = modified_file.source_code or "na"
                key = src_original + src_modified # the idea is comes from disticnt traning data sicne we pass this code, so focus on it
                #deduplicate based on this
                key_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
                if key_hash in seen_hashes:
                    logging.info(f"Skipping duplicate commit: {commit.hash}")
                    continue
                seen_hashes.add(key_hash) # deduplication
                # calculate domain sill vector for each commit message/ perf or nonperf
                domain_vector ="" #get_domain_vector(commit_message,code_diff)
                
                commit_info_dev = {
                    'md5hash': key_hash,
                    'dev_email': commit_dev_email,
                    'dev_name': commit_dev_name,
                    'url': commit_url,
                    'added_lines': n_added_lines,
                    'deleted_lines': n_deleted_lines,
                    'domain_vec': domain_vector,
                    'pred': pred
                }                
                
                commit_dev_exp.append(commit_info_dev)
                
                if len(commit_dev_exp) == 5000:
                    batch_id_dev += 1
                    # call upload function
                    #write_commit_data_to_file_and_upload_dev(namespace, bucket_name_dev, results_dir) # give the new bucket name for separating storage of dev exp
                    
                    
                    
                
                
                if 'merge' in commit_message or 'revert' in commit_message:
                    logging.info(f"Skipping merge commit: {commit.hash}")
                    continue
                

                
                
                
                # the rest is for perf only, saving performance data
                
                if  no_changed_files == 1 and pred: # and get_prediction_mistral(commit_message): #get_prediction(commit_message) == 'LABEL_1':
                    

                    if modified_file.change_type not in ["ADD", "DELETE"]:
                        no_modified_method = len(modified_file.changed_methods)
                        if  no_modified_method == 1:

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
                            orig_method_loc_start = changed_method_loc_start
                            orig_method_loc_end = changed_method_loc_end
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
                                'md5hash': key_hash,
                                'project_name': commit.project_name,
                                'commit_url': commit_url + '/commit/' + commit.hash,
                                'commit_message': commit_message,
                                'filename': filename,
                                'commit_date': str(commit.committer_date),
                                'author_email': author.email,
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
                            #seen_hashes.add(key_hash) no need here because we are doing it at the beginning
                            total_found += 1
                            local_commit_counter += 1
                            logging.info(f"Total perf found: {total_found}")

                            if len(commit_data) == data_threshold:
                                batch_id += 1
                                #write_commit_data_to_file()
                                #write_commit_data_to_file_and_upload(namespace, bucket_name, results_dir)
                        
                elif no_changed_files > 1 and pred:
                    commit_info = {
                        'url': commit_url,
                        'n_chaged_file': no_changed_files
                    }
                    # add this commit info to running list
                    commit_data_url.append(commit_info)
                    if len(commit_data_url) == data_threshold:
                        batch_id_url += 1
                        #write_commit_data_to_file()
                        #write_commit_data_to_file_and_upload_url(namespace, bucket_name, results_dir)
        
            except Exception as commit_error:
                logging.error(f"Error processing commit '{commit.hash}' in repository '{repo_url}': {commit_error}")
                # Continue to the next commit despite the error
                continue
        repo_counter_success += 1
        return True
    except Exception as repo_error:
        repo_counter_fail += 1
        logging.error(f"Error while accessing repository '{repo_url}': {repo_error}")
        return True
        
        # Continue to the next repository despite the error

    finally:
        end_time = time.time()  # End time for the current repository
        time_taken = end_time - start_time
        logging.info(f"Time taken for processing {repo_url}: {time_taken} seconds")
        logging.info(f"local_commit_found (perf/nperf):{local_commit_counter}/{local_commit_counter_url}: {repo_url}")

def main():
    global batch_id
    global batch_id_url
    global batch_id_dev
    global total_found
    global total_found_url
    global commit_data
    global commit_data_url
    global commit_dev_exp
    global repo_counter_fail
    global repo_counter_success
    logging.info("Starting mining..")

    repo_url = 'https://github.com/trilinos/Trilinos'
    result = mine_repo_commits(repo_url) 
    logging.info(f"R:{result}")

if __name__ == "__main__":
    main()
