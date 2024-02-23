#!/bin/bash

# Path to the file containing the list of VM hostnames or IPs
HOSTS_FILE="sshhosts"

# File to check for on the remote hosts
CHECK_FILE="/home/ubuntu/miner_github/analyzer/script_complete.txt"

# Time to wait between checks (in seconds)
SLEEP_DURATION=300 # Example: 300 seconds = 5 minutes

while : ; do
    echo "Checking for $CHECK_FILE on all hosts..."

    # Execute the check command on all hosts listed in HOSTS_FILE
    parallel-ssh -i -h "$HOSTS_FILE" -t 10 "test -f $CHECK_FILE && echo 'File exists' || echo 'File not found'"

    # Optional: Process output here if needed, for example, to determine if all hosts have completed.

    echo "Waiting for $SLEEP_DURATION seconds before re-checking..."
    sleep $SLEEP_DURATION
done
