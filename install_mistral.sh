#!/bin/bash
# Initialize Conda for script use
# Using parallel-ssh to install Python packages on all hosts

parallel-ssh -i -h sshhosts -t 0 'pip3 install langchain -y'
parallel-ssh -i -h sshhosts -t 0 'pip3 install bitsandbytes -y'
parallel-ssh -i -h sshhosts -t 0 'sudo apt install git-lfs'
parallel-ssh -i -h sshhosts -t 0 'git clone https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2'
parallel-ssh -i -h sshhosts -t 0 'cd  Mistral-7B-Instruct-v0.2/ && git lfs fetch -y && git lfs pull -y'
echo "Testing mistral...."
sleep 5
parallel-ssh -i -h sshhosts -t 0 'python home/ubuntu/miner_github/test_mistral7b.py' 
