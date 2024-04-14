#!/bin/bash
# Initialize Conda for script use
# Using parallel-ssh to install Python packages on all hosts

pip3 install langchain 
pip3 install bitsandbytes 
sudo apt install git-lfs -y
git clone https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
cd  Mistral-7B-Instruct-v0.2/ 
git lfs fetch 
git lfs pull 
echo "Testing mistral...."
sleep 5
/home/ubuntu/miniforge3/bin/python home/ubuntu/miner_github/test_mistral7b.py
