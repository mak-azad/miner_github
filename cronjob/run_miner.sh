#!/bin/bash

# The command or script you want to check
COMMAND="miner_github/analyzer/test_repo_analyzer.py" #python miner_github/analyzer/test_repo_analyzer.py
# Use pgrep and the name of your script to check if it's running
if /usr/bin/pgrep -f $COMMAND > /dev/null
then
    echo "$COMMAND is running."
else
    echo "$COMMAND is not running. Starting $COMMAND..."
    # Starting the script in the background
    source miniforge3/bin/activate mytoolenv 
    python miner_github/analyzer/test_repo_analyzer.py > /dev/null 2> error_log.txt || echo "Command failed on $(hostname)" >> error_log.txt &
    echo "$COMMAND started."
fi
