#!/bin/bash
# Initialize Conda for script use
# Using parallel-ssh to install Python packages on all hosts

pip3 install langchain -y
pip3 install bitsandbytes -y
sudo apt install git-lfs -y
git clone https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
cd  Mistral-7B-Instruct-v0.2/ 
git lfs fetch -y
git lfs pull -y
echo "Testing mistral...."
sleep 5
python home/ubuntu/miner_github/test_mistral7b.py
