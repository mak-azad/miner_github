#!/bin/bash
# Initialize Conda for script use

source /home/ubuntu/miniforge3/etc/profile.d/conda.sh

# Create Conda environments
/home/ubuntu/miniforge3/bin/conda create -n mytoolenv python=3.10 -y

# Activate the environment
# Note: For script use, prefer this method over `conda activate`
source miniforge3/bin/activate mytoolenv

# Follow-up commands that require the Conda environment can go here
echo "Installing Python packages (pydriller, pygit2, pandas) on all hosts..."
sleep 5
pip3 install pydriller pygit2 pandas nltk
echo "Installing OCI"
pip3 install oci
echo "Installing ML related libs..."
sleep 5
echo "Installing pytorch.."
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121
echo "torch installation complete, checking .."
sleep 3
python3 -c "import torch; print(torch.__version__)"
sleep 5
python3 -c "import torch; print(torch.cuda.is_available())"
sleep 10
echo "Installing transformers.."
pip3 install transformers
pip3 install accelerate
echo "Now test the model.."
sleep 3
python3 miner_github/test_model.py


echo "Now going to setup OCI client..."
# Create the .oci directory in the home directory if it doesn't already exist
mkdir -p ~/.oci
sleep 5
echo "Copying OCI credentials...."
cp /home/ubuntu/miner_github/file.pem .oci/
# OCI configuration details
oci_user_ocid="ocid1.user.oc1..aaaaaaaantmgpywouidjiiw33kdpnlcadmdgsqotqwvwwtzfbna76hmwzwdq"
oci_fingerprint="26:2d:ef:f3:9c:ff:93:42:97:36:05:70:06:a1:72:48"
oci_tenancy_ocid="ocid1.tenancy.oc1..aaaaaaaar6oqqngegbs2tthc4vjzm3ruzvrddsof45yknta2oo6jmkvcgk5q"
oci_region="us-ashburn-1"
oci_key_file="/home/ubuntu/miner_github/file.pem" # Ensure this path is correct and accessible

# Write the config file. Adjust the path to the key file as necessary.
cat > ~/.oci/config << EOF
[DEFAULT]
user=${oci_user_ocid}
fingerprint=${oci_fingerprint}
tenancy=${oci_tenancy_ocid}
region=${oci_region}
key_file=${oci_key_file}
EOF

# Set file permissions to be read-only by the file's owner
#chmod 600 ~/.oci/config
echo "OCI configuration written to ~/.oci/config"
# echo "Installing mistral.."
# sleep 5
# pip3 install langchain 
# pip3 install bitsandbytes 
# sudo apt install git-lfs -y
# rm -rf  Mistral-7B-Instruct-v0.2/
# git clone https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
# cd  Mistral-7B-Instruct-v0.2/ 
# git lfs fetch 
# git lfs pull 
# cd ..
# echo "Testing mistral...."
# sleep 5
# python3 miner_github/test_mistral.py

# #echo "Testing cloud storage.."
# #python3 miner_github/test_oci_store2.py 
# echo "Running the miner...."
# sleep 5
# python3 miner_github/analyzer/repo_analyzer.py

# echo "Script execution completed at slave"