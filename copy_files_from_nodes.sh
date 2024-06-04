#!/bin/bash

# Define the remote directory you want to copy files from
remote_directory="/home/ubuntu/miner_github/analyzer/"
local_directory="/home/ubuntu/tmp/partial_work/"

# Create local directory if it doesn't exist
mkdir -p "$local_directory"

# Read the IP addresses from the sshhosts file and copy the files from each node to the local directory
while read -r node_ip; do
    echo "Copying from $node_ip..."
    remote_file="${remote_directory}github_repositories_${node_ip}.csv"
    scp ubuntu@"$node_ip":"$remote_file" "$local_directory"
    if [ $? -eq 0 ]; then
        echo "Successfully copied $(basename "$remote_file") from $node_ip"
    else
        echo "Failed to copy $(basename "$remote_file") from $node_ip" >&2
    fi
done < sshhosts
