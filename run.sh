#!/bin/bash
echo "Spliting task to all nodes..."
python3 task_parallelizer.py repository_lists/github_repositories_C++_12232023.csv ubuntu
echo "Now running the analyzer script.."
parallel-ssh -i -h sshhosts -t 0 'python3 miner_github/analyzer/repo_analyzer.py'