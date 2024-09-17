import requests

# Replace with your GitHub personal access token
GITHUB_TOKEN = "token"
# Replace with the repository owner and name
REPO_OWNER = "molpopgen" #"SerenityOS"
REPO_NAME = "fwdpp"#"serenity"
# Replace with the exact issue number you want to search for (with #)
ISSUE_NUMBER = "#231"

# GitHub GraphQL API URL
url = "https://api.github.com/graphql"

# GraphQL query to search pull requests with the exact issue number in title or body
query = """
{
  search(query: "repo:%s/%s is:pr '%s'", type: ISSUE, first: 100) {
    edges {
      node {
        ... on PullRequest {
          title
          body
          url
        }
      }
    }
  }
}
""" % (REPO_OWNER, REPO_NAME, ISSUE_NUMBER)

# Headers including the authorization token
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

# Making the request to the GitHub GraphQL API
response = requests.post(url, json={'query': query}, headers=headers)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()
    # Parsing and printing the relevant pull requests
    pull_requests = data['data']['search']['edges']
    if pull_requests:
        if len(pull_requests) == 1: 
            
            for pr in pull_requests:
                pr_node = pr['node']
                print(f"Title: {pr_node['title']}")
                print(f"Body: {pr_node['body']}")
                print(f"URL: {pr_node['url']}")
                print("-" * 50)
        else:
            print("No pull requests found.")
else:
    print(f"Query failed with status code {response.status_code}: {response.text}")
