import requests

# Replace these with your repository details
OWNER = 'ClickHouse'
REPO = 'ClickHouse'
TOKEN = 'token'  # You will need a GitHub token for authenticated requests

# Set up headers for authenticated requests
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Step 1: Get all closed issues with the label 'performance'
def get_issues_with_performance_label():
    issues = []
    page = 1
    while True:
        url = f'https://api.github.com/repos/{OWNER}/{REPO}/issues'
        params = {
            'state': 'closed',
            'labels': 'performance',
            'per_page': 100,
            'page': page
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch issues: {response.status_code}")
            break
        
        page_issues = response.json()

        if not page_issues:
            break  # Exit loop when no more issues are returned

        issues.extend(page_issues)
        page += 1

    return issues

# Step 2: Check if the issue has only one linked PR using the Timeline Events API
def get_linked_prs(issue_number):
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue_number}/timeline'
    response = requests.get(url, headers=headers)
    timeline = response.json()

    prs = [event for event in timeline if event['event'] == 'cross-referenced' and 'pull_request' in event]
    return prs

# Step 3: Check if the PR has only one commit
def get_commit_count(pr_number):
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pr_number}/commits'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch commits for PR #{pr_number}: {response.status_code}")
        return 0

    commits = response.json()
    return len(commits)

# Putting it all together
def find_single_commit_pr_issues():
    issues = get_issues_with_performance_label()

    for issue in issues:
        issue_number = issue['number']
        prs = get_linked_prs(issue_number)
        if len(prs) == 1:  # Check if there's exactly one PR linked
            pr_number = prs[0]['pull_request']['number']
            commit_count = get_commit_count(pr_number)
            if commit_count == 1:  # Check if the PR has exactly one commit
                print(f"Issue #{issue_number} has one PR with one commit: PR #{pr_number}")
            else:
                print(f"Issue #{issue_number} has one PR with {commit_count} commits: PR #{pr_number}")
        else:
            print(f"Issue #{issue_number} has {len(prs)} linked PR(s)")

# Run the function to find PRs with exactly 1 commit
find_single_commit_pr_issues()
