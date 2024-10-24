# Mining Tool
## Running the tool
- `bash check.sh`
- `bash freeze_ubuntu.sh`
- `bash master.sh`
- `python3 task_parallelizer.py repository_lists/filtered_repositories_c.csv ubuntu`
- `parallel-ssh -i -h sshhosts -x "-oStrictHostKeyChecking=no" -P -t 0 'nohup bash /home/ubuntu/miner_github/install_n_run.sh'`
- `parallel-ssh -i -h sshhosts 'chmod +x miner_github/cronjob/add_cron_job.sh'`
- `parallel-ssh -i -h sshhosts 'bash miner_github/cronjob/add_cron_job.sh'`
- `parallel-ssh -i -h sshhosts -t 0 'source miniforge3/bin/activate mytoolenv && nohup python3 miner_github/analyzer/test_repo_analyzer.py > /dev/null 2> error_log.txt || echo "Command failed on $(hostname)" >> error_log.txt'`
- `parallel-ssh -i -h sshhosts 'ps aux | grep 'miner_github/analyzer/test_repo_analyzer.py' | grep -v grep'`
- Run `monitor_logs.py` to restart a node in case the script hangs 
- `parallel-ssh -i -h sshhosts 'pkill -9 -f "miner_github/analyzer/repo_analyzer.py"'`
## Collecting data from Ocacle Cloud Object Store Bucket
- Modify `/home/akazad/dataset/src/downloader_oci_bucket.py` @Lab
- Modify `bucket_name` `results_dir = '/home/akazad/dataset/python_perf'`  line 85: `part[0]` : which file to download

# Outdated readme 
## 1. Access the master node of your cluster and configure scripts
### Install Python 3.8
```
sudo apt-get update && sudo apt-get install -y software-properties-common && sudo add-apt-repository -y ppa:deadsnakes/ppa && sudo apt-get update && sudo apt-get install -y python3.8 && python3.8 --version
```

### Install pip for Python 3.8
```
sudo apt-get install -y python3.8-distutils && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python3.8 get-pip.py && pip3 --version
```

### Install required dependencies for our scripts
```
pip3 install pandas
```

## 2. Fetch github repositories and export in a CSV file
Use the following command to fetch repositories from github and export into the file `github_repositories.csv`
```
python repo_fetcher.py --language <LANGUAGE> --stars <MINIMUM_STARS> --forks <MINIMUM_FORKS> --last_commit <LAST_UPDATE_DATE> --result_limit <NUMBER_OF_REPO>
```

For example see the command below
```
python repo_fetcher.py --language Python --stars 20 --forks 0 --last_commit 2010-01-01 --result_limit 2000
```

You can run without any filter as the command below, then the script applies the above filters and no limit by default<br>
`python repo_fetcher.py`

## 3. Run the commit analyzer on multi-node cluster using parallel ssh
### Create the hosts file
Add all the node ip addresses line by line into the `sshhosts` file

### Ensure inter-node ssh permissions
Execute the authenticator scripts inside each nodes at first<br>
Run command: `sh authenticator.sh`

### Check if all worker nodes are accessible from the master node
Run the following command to using parallel-ssh to print the node names. Do not run any further `parallel` commands until this one executes sucessfully.
```
parallel-ssh -i -h sshhosts -O StrictHostKeyChecking=no hostname
```

### Install python3.8 in all worker nodes
Run the following command only if python3.8 not installed earlier
```
parallel-ssh -A -i -h sshhosts 'sudo apt-get update && sudo apt-get install -y software-properties-common && sudo add-apt-repository -y ppa:deadsnakes/ppa && sudo apt-get update && sudo apt-get install -y python3.8'
```
Check and confirm python3.8 version in all worker nodes
```
parallel-ssh -A -i -h sshhosts 'python3.8 --version'
```

### Install pip for python3.8 in all worker nodes
Run the following command only if pip for python3.8 not installed earlier
```
parallel-ssh -A -i -h sshhosts 'sudo apt-get install -y python3.8-distutils && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python3.8 get-pip.py'
```
Check and confirm pip version for python3.8 in all worker nodes
```
parallel-ssh -A -i -h sshhosts 'pip3 --version'
```

### Install required dependencies for our scripts
```
parallel-ssh -A -i -h sshhosts 'pip3 install pydriller pygit2'
```
Confirm the installations of required dependencies
```
parallel-ssh -A -i -h sshhosts 'pip3 show pydriller && pip3 show pygit2'
```

### Clone the github_miner repository in all nodes to upload the commit analysis results
```
parallel-ssh -i -h sshhosts 'git clone https://github.com/proywm/githubMiningCuda.git'
```

### Run script to split and distribute the input files among the nodes
```
python3.8 task_parallelizer.py your_repo_list your_username
```
For example
```
python3.8 task_parallelizer.py repository_lists/github_repositories_*.csv probirr
```

### Execute the analyzer on multiple nodes in parallel
Run the following command to execute the analyzer using parallel-ssh. If asked for password then skip by pressing enter key.
```
parallel-ssh -A -i -h sshhosts 'python3.8 githubMiningCuda/analyzer/repo_analyzer.py'
```

## 4. Collect the results from worker nodes and upload to GitHub
Run the following script to copy all the raw result files from the worker nodes to the master node, merge them into a single result file and upload to GitHub
```
python3.8 result_collector.py your_GitHub_PersonalAccessToken
```
