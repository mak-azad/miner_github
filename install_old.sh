#!/bin/bash

# Update system and install necessary packages for managing PPAs
echo "Updating system and installing software-properties-common..."
sudo apt-get update && sudo apt-get install -y software-properties-common

# Add deadsnakes PPA for Python 3.8
echo "Adding deadsnakes PPA for Python 3.8..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

# Update system and install Python 3.8
echo "Updating system again and installing Python 3.8..."
sudo apt-get update && sudo apt-get install -y python3.8

# Display the installed Python version
echo "Python version installed:"
python3.8 --version

# Install Python 3.8 distutils, required for pip installation
echo "Installing python3.8-distutils..."
sudo apt-get install -y python3.8-distutils

# Download get-pip.py script and install pip for Python 3.8
echo "Downloading get-pip.py and installing pip for Python 3.8..."
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python3.8 get-pip.py

# Display the installed pip version
echo "Pip version installed:"
pip3 --version

# Install pssh for running SSH commands in parallel
echo "Installing parallel ssh (pssh)..."
sudo apt-get install -y pssh

# Using parallel-ssh to update and install Python 3.8 on multiple hosts
echo "Updating and installing Python 3.8 on all hosts listed in sshhosts..."
parallel-ssh -i -h sshhosts 'sudo apt-get update && sudo apt-get install -y software-properties-common && sudo add-apt-repository -y ppa:deadsnakes/ppa && sudo apt-get update && sudo apt-get install -y python3.8'

# Using parallel-ssh to install Python packages on all hosts
echo "Installing Python packages (pydriller, pygit2, pandas) on all hosts..."
parallel-ssh -i -h sshhosts -t 0 'pip3 install pydriller pygit2 pandas nltk'


echo "Installing ML related libs..."
sleep 5
echo "Installing pytorch.."
parallel-ssh -i -h sshhosts -t 0 'pip3 install torch' # -t 0 for no time bound
echo "torch installation complete, checking .."
parallel-ssh -i -h sshhosts 'python3 -c "import torch; print(torch.__version__)"'
echo "Installing transformers.."
parallel-ssh -i -h sshhosts -t 0 'pip3 install transformers'
sleep 5
echo "cleaning previous version.."
parallel-ssh -i -h sshhosts 'sudo rm -rf  miner_github/'
echo "Cloning repo to all nodes home directory"
parallel-ssh -i -h sshhosts 'git clone https://github.com/mak-azad/miner_github.git'

echo "Now test the model on all nodes.."
sleep 5
parallel-ssh -i -h sshhosts 'python3 miner_github/test_model.py'
echo "Script execution completed."

