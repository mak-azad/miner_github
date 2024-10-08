#!/bin/bash

# Define the file you want to copy
file_to_copy="/home/ubuntu/tmp/analyzer/test_repo_analyzer.py"
remote_directory="/home/ubuntu/miner_github/analyzer/"

# Read the IP addresses from the sshhosts file and copy the file to each node
while read -r node_ip; do
    echo "Copying to $node_ip..."
    scp "$file_to_copy" ubuntu@"$node_ip":"$remote_directory"
    if [ $? -eq 0 ]; then
        echo "Successfully copied to $node_ip"
    else
        echo "Failed to copy to $node_ip" >&2
    fi
done < sshhosts
