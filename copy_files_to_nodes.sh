#!/bin/bash

# Define the file you want to copy
file_to_copy="/home/ubuntu/tmp/update_state.py"
remote_directory="/home/ubuntu/miner_github"

# Read the IP addresses from the sshhosts file and copy the file to each node
while read -r node_ip; do
    scp "$file_to_copy" ubuntu@"$node_ip":"$remote_directory"
done < sshhosts