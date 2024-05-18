#!/bin/bash

# Define the file you want to copy
file_to_copy="/users/akazad/tmp/analyzer/test_repo_analyzer.py"
remote_directory="/users/akazad/miner_github/analyzer"

# Read the IP addresses from the sshhosts file and copy the file to each node
while read -r node_ip; do
    scp "$file_to_copy" akazad@"$node_ip":"$remote_directory"
done < sshhosts