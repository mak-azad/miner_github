from pydriller import Repository
import csv

# Replace these with your repository path and specific commit hash
# repo_path = 'https://github.com/AMReX-Astro/Nyx'
# commit_hash = '5658ac4363431c0d96a854bb9d1412b44a105117'

# https://github.com/bw2012/UnrealSandboxTerrain/commit/38af74030a717cb5191c4b1e1a9c72122fbe545d

#https://github.com/herumi/bls/commit/b1d7cd63175960edb7e107ef0be2ac2c78453c18
#https://github.com/snucrypto/HEAAN/commit/0e2ab8d2968d97e7f792d05f3c32a1448c415308
#https://github.com/TeamHypersomnia/rectpack2D/commit/174844097227bf84f9c99583cd74eb80278e9fc2




def read_links_from_csv_to_list(csv_file_path):
    commits_list = []  # Initialize an empty list

    with open(csv_file_path, mode='r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            repo_url = row['repo_url']
            commit_hash = row['commit_hash']
            
            # Skip rows where 'Repo URL' indicates no commit URL was found
            if repo_url != "No commit_url found":
                # Append a new dictionary with 'repo_url' and 'commit_hash' keys to the list
                commits_list.append({'repo_url': repo_url, 'commit_hash': commit_hash})
    
    return commits_list

# Example usage
csv_file_path = '/home/akazad/data/output_file.csv'
commits_list = read_links_from_csv_to_list(csv_file_path)

# Now, commits_list is a list where each item is a dictionary with 'repo_url' and 'commit_hash'.


# # Example usage
# csv_file_path = '/home/akazad/data/output_file.csv'
# commits_info = read_links_from_csv_to_dict(csv_file_path)

# Now, commits_info is a dictionary where each key is a repository URL and its value is the corresponding commit hash.


# Now, repo_urls and commit_hashes are lists containing the repository URLs and commit hashes, respectively.





repo_path = 'https://github.com/TeamHypersomnia/rectpack2D'
commit_hash = '174844097227bf84f9c99583cd74eb80278e9fc2'



for ci in commits_list:
    for commit in Repository(ci['repo_url'], single=ci['commit_hash']).traverse_commits():
        for modified_file in commit.modified_files:
            methods = modified_file.methods_before
            for changed_method in modified_file.changed_methods:
                method_name = changed_method.name
                for m in methods:
                    if m == changed_method:
                        print("FOUND")
                        pre_m_start = m.start_line
                        pre_m_end = m.end_line
                        # print(m.start_line)
                        # print(m.end_line)
                start_line = changed_method.start_line
                end_line = changed_method.end_line
                
                # Extract method body from BEFORE change
                if modified_file.source_code_before:
                    lines_before = modified_file.source_code_before.split('\n')
                    #lines_before = modified_file.source_code_before
                    method_body_before = '\n'.join(lines_before[pre_m_start-1:pre_m_end])
                    print(f"Method {method_name} BEFORE change:\n{method_body_before}\n")
                
                # Extract method body from AFTER change
                if modified_file.source_code:
                    lines_after = modified_file.source_code.split('\n')
                    #lines_after = modified_file.source_code
                    method_body_after = '\n'.join(lines_after[start_line-1:end_line])
                    print(f"Method {method_name} AFTER change:\n{method_body_after}\n")
