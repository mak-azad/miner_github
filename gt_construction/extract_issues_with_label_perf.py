import csv
import requests
from requests.utils import quote
import time

# Set up your GitHub personal access token
GITHUB_TOKEN = "token"
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

def check_rate_limit(response):
    """
    Check the GitHub API rate limit from the response headers and wait if necessary.

    Args:
        response (requests.Response): The response object from a GitHub API request.
    """
    rate_limit = int(response.headers['X-RateLimit-Limit'])
    rate_limit_remaining = int(response.headers['X-RateLimit-Remaining'])
    reset_time = int(response.headers['X-RateLimit-Reset'])
    
    if rate_limit_remaining == 0:
        sleep_time = reset_time - int(time.time()) + 5  # Adding 5 seconds buffer to ensure reset
        print(f"Rate limit exceeded. Waiting for {sleep_time} seconds until reset.")
        time.sleep(sleep_time)
    else:
        print(f"Rate Limit - Remaining: {rate_limit_remaining}, Limit: {rate_limit}, Resets at (UTC): {reset_time}")

def fetch_closed_performance_issues(repo_url):
    """
    Fetch closed issues labeled 'performance' from a GitHub repository.

    Args:
        repo_url (str): URL of the GitHub repository.

    Returns:
        List of dictionaries containing issue numbers and URLs.
    """
    repo = repo_url.replace("https://github.com/", "").rstrip("/")
    issues = []
    page = 1
    query = f'repo:{repo} is:issue is:closed label:performance'

    encoded_query = quote(query)

    while True:
        url = f"https://api.github.com/search/issues?q={encoded_query}&page={page}&per_page=100"
        print(f"Fetching issues from URL: {url}")
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Check rate limit based on response headers
            check_rate_limit(response)
            
            fetched_issues = response.json()['items']
            if not fetched_issues:
                break
            issues.extend(fetched_issues)
            page += 1
        else:
            print(f"Failed to fetch issues for {repo}, status code {response.status_code}")
            print(response.json())
            break

    return [{'number': issue['number'], 'issue_url': issue['html_url']} for issue in issues]

def process_repositories(input_csv_file, output_csv_file):
    """
    Read repository URLs from a CSV file, fetch closed performance issues, and save results to another CSV file.

    Args:
        input_csv_file (str): Path to the input CSV file containing repository URLs.
        output_csv_file (str): Path to the output CSV file to save the results.
    """
    # Read the repository URLs from the input CSV file with a 'url' field
    with open(input_csv_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)  # Use DictReader to read CSV with headers
        repo_urls = [row['url'] for row in reader if row['url']]  # Extract URLs from the 'url' column

    batch_size = 10  # Example batch size
    for i in range(0, len(repo_urls), batch_size):
        batch = repo_urls[i:i + batch_size]
        for repo_url in batch:
            performance_issues = fetch_closed_performance_issues(repo_url)
            number_of_issues = len(performance_issues)
            issue_numbers = [issue['number'] for issue in performance_issues]

            # Write the results to the output CSV file immediately
            if number_of_issues > 0:
                with open(output_csv_file, mode='a', newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow([repo_url, number_of_issues] + issue_numbers)
            
        # Pause between batches to avoid hitting the rate limit too quickly
        print("Pausing for 1 second between batches to avoid rate limit...")
        time.sleep(1)

# Example usage
input_csv_file = 'filteredc.csv'  # Input CSV file with repo URLs
output_csv_file = 'label_perf_issues_c.csv'  # Output CSV file to save results

# Initialize output CSV file with header
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['repo_url', 'number_of_issues', 'issue_numbers'])

process_repositories(input_csv_file, output_csv_file)
            
print(f"Processed repositories and saved results to {output_csv_file}.")
