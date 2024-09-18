import csv
import requests
import time

# Set up your GitHub personal access token
GITHUB_TOKEN = "token"
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

# GitHub GraphQL API URL
graphql_url = "https://api.github.com/graphql"



import time

def check_rate_limit():
    """
    Check the current GitHub API rate limit using GraphQL.
    If the rate limit is exceeded, wait for 60 seconds before proceeding.
    """
    rate_limit_query = """
    {
      rateLimit {
        limit
        cost
        remaining
        resetAt
      }
    }
    """
    
    response = requests.post(graphql_url, json={'query': rate_limit_query}, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        rate_limit = data['data']['rateLimit']
        remaining = rate_limit['remaining']
        reset_time = rate_limit['resetAt']
        
        if remaining == 0:
            # Hardcode the sleep time to 60 seconds
            print(f"Rate limit exceeded. Sleeping for 3600 seconds before retrying.")
            time.sleep(3601)  # Hardcoded sleep for 60 seconds
        else:
            print(f"Rate Limit - Remaining: {remaining}, Limit: {rate_limit['limit']}, Resets at (UTC): {reset_time}")
    else:
        print(f"Failed to check rate limit. Status code: {response.status_code}")

# def check_rate_limit():
#     """
#     Check the current GitHub API rate limit using GraphQL.
#     """
#     rate_limit_query = """
#     {
#       rateLimit {
#         limit
#         cost
#         remaining
#         resetAt
#       }
#     }
#     """
    
#     response = requests.post(graphql_url, json={'query': rate_limit_query}, headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         rate_limit = data['data']['rateLimit']
#         remaining = rate_limit['remaining']
#         reset_time = rate_limit['resetAt']
        
#         if remaining == 0:
#             reset_timestamp = int(time.mktime(time.strptime(reset_time, "%Y-%m-%dT%H:%M:%SZ")))
#             sleep_time = reset_timestamp - int(time.time()) + 5  # Adding 5 seconds buffer
#             print(f"Rate limit exceeded. Waiting for {sleep_time} seconds until reset.")
#             time.sleep(sleep_time)
#         else:
#             print(f"Rate Limit - Remaining: {remaining}, Limit: {rate_limit['limit']}, Resets at (UTC): {reset_time}")
#     else:
#         print(f"Failed to check rate limit. Status code: {response.status_code}")


def find_prs_for_issue(repo_owner, repo_name, issue_number, output_csv_file):
    """
    Find pull requests that mention a specific issue number using the GraphQL API,
    and only print PRs if there is exactly one PR, it has exactly one commit, and
    the issue number is mentioned as '#issue_number' (with the # symbol).
    
    Args:
        repo_owner (str): Owner of the GitHub repository.
        repo_name (str): Name of the GitHub repository.
        issue_number (str): The issue number to search for in pull requests.
        output_csv_file (str): Path to the output CSV file to save the results.
    """
    
    # Corrected GraphQL query to fetch the commit URL from the commit object
    query = """
    {
      search(query: "repo:%s/%s is:pr '%s'", type: ISSUE, first: 100) {
        edges {
          node {
            ... on PullRequest {
              title
              bodyText
              url
              commits(first: 1) {
                totalCount
                nodes {
                  commit {
                    url  # Correct field to get the commit URL
                  }
                }
              }
            }
          }
        }
      }
    }
    """ % (repo_owner, repo_name, issue_number)

    # Send the GraphQL request
    response = requests.post(graphql_url, json={'query': query}, headers=headers)
    
    try:
        response_json = response.json()
        
        # Check if 'data' exists in the response
        if 'data' not in response_json:
            print(f"Error in response: {response_json}")
            return
        
        prs = response_json['data']['search']['edges']
        check_rate_limit()  # Check rate limit after each request

        # Proceed only if there is exactly one PR
        if len(prs) == 1:
            pr_node = prs[0]['node']
            pr_url = pr_node['url']
            pr_title = pr_node['title']
            pr_body = pr_node['bodyText']
            commit_count = pr_node['commits']['totalCount']

            # Proceed only if the PR has exactly one commit
            if commit_count == 1:
                # Filter out PRs where the issue number isn't mentioned as '#issue_number'
                if f"#{issue_number}" in pr_title or f"#{issue_number}" in pr_body:
                    # Get the commit URL from the correct field
                    commit_url = pr_node['commits']['nodes'][0]['commit']['url']
                    print(f"PR Title: {pr_title}, PR URL: {pr_url}, Commit URL: {commit_url}, Commit Count: {commit_count}")
                    
                    # Write the result to the output CSV
                    with open(output_csv_file, mode='a', newline='', encoding='utf-8') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerow([repo_owner, repo_name, issue_number, pr_url, commit_url])
                else:
                    print(f"PR {pr_url} mentions issue {issue_number} but not with '#'. Skipping...")
            else:
                print(f"PR {pr_url} has {commit_count} commits. Skipping...")
        else:
            print(f"Found {len(prs)} PRs for issue #{issue_number}. Skipping...")
    
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
        print(f"Response text: {response.text}")
    except KeyError as e:
        print(f"Unexpected response structure, missing key: {e}")
        print(f"Response JSON: {response_json}")
    except Exception as e:
        print(f"An error occurred: {e}")


def find_prs_for_issue2(repo_owner, repo_name, issue_number, output_csv_file):
    """
    Find pull requests that mention a specific issue number using the GraphQL API,
    and only print PRs if there is exactly one PR and it has exactly one commit.
    
    Args:
        repo_owner (str): Owner of the GitHub repository.
        repo_name (str): Name of the GitHub repository.
        issue_number (str): The issue number to search for in pull requests.
        output_csv_file (str): Path to the output CSV file to save the results.
    """
    
    # Corrected GraphQL query to fetch the commit URL from the commit object
    query = """
    {
      search(query: "repo:%s/%s is:pr '#%s'", type: ISSUE, first: 100) {
        edges {
          node {
            ... on PullRequest {
              title
              url
              commits(first: 1) {
                totalCount
                nodes {
                  commit {
                    url  # Correct field to get the commit URL
                  }
                }
              }
            }
          }
        }
      }
    }
    """ % (repo_owner, repo_name, issue_number)

    # Send the GraphQL request
    response = requests.post(graphql_url, json={'query': query}, headers=headers)
    
    try:
        response_json = response.json()
        
        # Check if 'data' exists in the response
        if 'data' not in response_json:
            print(f"Error in response: {response_json}")
            return
        
        prs = response_json['data']['search']['edges']
        check_rate_limit()  # Check rate limit after each request

        # Proceed only if there is exactly one PR
        if len(prs) == 1:
            pr_node = prs[0]['node']
            pr_url = pr_node['url']
            pr_title = pr_node['title']
            commit_count = pr_node['commits']['totalCount']
            
            # Proceed only if the PR has exactly one commit
            if commit_count == 1:
                # Get the commit URL from the correct field
                commit_url = pr_node['commits']['nodes'][0]['commit']['url']
                print(f"PR Title: {pr_title}, PR URL: {pr_url}, Commit URL: {commit_url}, Commit Count: {commit_count}")
                
                # Write the result to the output CSV
                with open(output_csv_file, mode='a', newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([repo_owner, repo_name, issue_number, pr_url, commit_url])
            else:
                print(f"PR {pr_url} has {commit_count} commits. Skipping...")
        else:
            print(f"Found {len(prs)} PRs for issue #{issue_number}. Skipping...")
    
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
        print(f"Response text: {response.text}")
    except KeyError as e:
        print(f"Unexpected response structure, missing key: {e}")
        print(f"Response JSON: {response_json}")
    except Exception as e:
        print(f"An error occurred: {e}")


        
        
# def find_prs_for_issue(repo_owner, repo_name, issue_number, output_csv_file):
#     """
#     Find pull requests that mention a specific issue number using the GraphQL API,
#     and only print PRs if there is exactly one PR and it has exactly one commit.
    
#     Args:
#         repo_owner (str): Owner of the GitHub repository.
#         repo_name (str): Name of the GitHub repository.
#         issue_number (str): The issue number to search for in pull requests.
#         output_csv_file (str): Path to the output CSV file to save the results.
#     """
    
#     # GraphQL query to search for pull requests mentioning the issue number and fetch the number of commits
#     query = """
#     {
#       search(query: "repo:%s/%s is:pr '#%s'", type: ISSUE, first: 100) {
#         edges {
#           node {
#             ... on PullRequest {
#               title
#               url
#               commits {
#                 totalCount
#               }
#             }
#           }
#         }
#       }
#     }
#     """ % (repo_owner, repo_name, issue_number)

#     # Send the GraphQL request
#     response = requests.post(graphql_url, json={'query': query}, headers=headers)
    
#     if response.status_code == 200:
#         prs = response.json()['data']['search']['edges']
#         check_rate_limit()  # Check rate limit after each request

#         # Proceed only if there is exactly one PR
#         if len(prs) == 1:
#             pr_node = prs[0]['node']
#             pr_url = pr_node['url']
#             pr_title = pr_node['title']
#             commit_count = pr_node['commits']['totalCount']
            
#             # Proceed only if the PR has exactly one commit
#             if commit_count == 1:
#                 print(f"PR Title: {pr_title}, PR URL: {pr_url}, Commit Count: {commit_count}")
                
#                 # Write the result to the output CSV
#                 with open(output_csv_file, mode='a', newline='', encoding='utf-8') as outfile:
#                     writer = csv.writer(outfile)
#                     writer.writerow([repo_owner, repo_name, issue_number, pr_url])
#             else:
#                 print(f"PR {pr_url} has {commit_count} commits. Skipping...")
#         else:
#             print(f"Found {len(prs)} PRs for issue #{issue_number}. Skipping...")
#     else:
#         print(f"Failed to fetch pull requests for issue #{issue_number}. Status code: {response.status_code}")
#         check_rate_limit()  # Check rate limit even if the request fails


# def find_prs_for_issue(repo_owner, repo_name, issue_number, output_csv_file):
#     """
#     Find pull requests that mention a specific issue number using the GraphQL API.
    
#     Args:
#         repo_owner (str): Owner of the GitHub repository.
#         repo_name (str): Name of the GitHub repository.
#         issue_number (str): The issue number to search for in pull requests.
#         output_csv_file (str): Path to the output CSV file to save the results.
#     """
    
#     # GraphQL query to search for pull requests mentioning the issue number
#     query = """
#     {
#       search(query: "repo:%s/%s is:pr '#%s'", type: ISSUE, first: 100) {
#         edges {
#           node {
#             ... on PullRequest {
#               title
#               url
#             }
#           }
#         }
#       }
#     }
#     """ % (repo_owner, repo_name, issue_number)

#     # Send the GraphQL request
#     response = requests.post(graphql_url, json={'query': query}, headers=headers)
    
#     if response.status_code == 200:
#         prs = response.json()['data']['search']['edges']
#         check_rate_limit()  # Check rate limit after each request

#         if prs:
#             for pr in prs:
#                 pr_node = pr['node']
#                 pr_url = pr_node['url']
#                 pr_title = pr_node['title']
                
#                 print(f"PR Title: {pr_title}, PR URL: {pr_url}")
                
#                 # Write the result to the output CSV
#                 with open(output_csv_file, mode='a', newline='', encoding='utf-8') as outfile:
#                     writer = csv.writer(outfile)
#                     writer.writerow([repo_owner, repo_name, issue_number, pr_url])
#         else:
#             print(f"No pull requests found for issue #{issue_number}")
#     else:
#         print(f"Failed to fetch pull requests for issue #{issue_number}. Status code: {response.status_code}")
#         check_rate_limit()  # Check rate limit even if the request fails

def process_repositories_and_issues_from_file(input_csv_file, output_csv_file):
    """
    Read repository URLs and issue numbers from a CSV file, find pull requests for each issue, and save results to another CSV file.

    Args:
        input_csv_file (str): Path to the input CSV file containing repository URLs and issue numbers.
        output_csv_file (str): Path to the output CSV file to save the results.
    """
    # Read the repository URLs and issue numbers from the input CSV file
    with open(input_csv_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row:  # Ensure the row is not empty
                repo_url = row[0]  # The repository URL is in the first column
                issue_count = int(row[1])  # The number of issues is in the second column
                issue_numbers = row[2:2 + issue_count]  # The issue numbers follow

                # Extract owner and repo name from the repository URL
                #repo_owner, repo_name = repo_url.replace("https://github.com/", "").split('/')
                
                # Validate and extract owner and repo name from the repository URL
                if "https://github.com/" in repo_url:
                    repo_parts = repo_url.replace("https://github.com/", "").split('/')
                    if len(repo_parts) == 2:
                        repo_owner, repo_name = repo_parts
                    else:
                        print(f"Invalid repository URL format: {repo_url}. Skipping...")
                        continue  # Skip this row if the repo URL is malformed
                else:
                    print(f"Invalid repository URL format: {repo_url}. Skipping...")
                    continue  # Skip this row if the repo URL is malformed


                # Process each issue number for the current repository URL
                for issue_number in issue_numbers:
                    find_prs_for_issue(repo_owner, repo_name, issue_number, output_csv_file)

# Example usage
input_csv_file = 'data.csv'  # Input CSV file with repo URLs and issue numbers
output_csv_file = 'pr_commits_for_issues_graphql.csv'  # Output CSV file to save results

# Initialize output CSV file with header
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['repo_owner', 'repo_name', 'issue_number', 'pr_url'])

process_repositories_and_issues_from_file(input_csv_file, output_csv_file)

print(f"Processed repositories from {input_csv_file} and saved results to {output_csv_file}.")
