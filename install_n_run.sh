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
echo "Installing ML related libs..."
sleep 5
echo "Installing pytorch.."
pip3 install torch
echo "torch installation complete, checking .."
sleep 3
python3 -c "import torch; print(torch.__version__)"
sleep 3
echo "Installing transformers.."
pip3 install transformers
echo "Now test the model.."
sleep 3
python3 miner_github/test_model.py


echo "Now going to setup OCI client..."
# Create the .oci directory in the home directory if it doesn't already exist
mkdir -p ~/.oci
sleep 5
echo "Copying OCI credentials...."
cp miner_github/file.pem .oci/
# OCI configuration details
oci_user_ocid="ocid1.user.oc1..aaaaaaaantmgpywouidjiiw33kdpnlcadmdgsqotqwvwwtzfbna76hmwzwdq"
oci_fingerprint="26:2d:ef:f3:9c:ff:93:42:97:36:05:70:06:a1:72:48"
oci_tenancy_ocid="ocid1.tenancy.oc1..aaaaaaaar6oqqngegbs2tthc4vjzm3ruzvrddsof45yknta2oo6jmkvcgk5q"
oci_region="us-ashburn-1"
oci_key_file="miner_github/file.pem" # Ensure this path is correct and accessible

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

echo "Testing cloud storage.."
python3 miner_github/test_oci_store2.py 



echo "Script execution completed at slave"