import paramiko
import time
from datetime import datetime, timedelta
import csv

# Define the file containing the hosts
hosts_file = "t.txt"
# The script generating the log
script_to_kill = "miner_github/analyzer/test_repo_analyzer.py"
# The log directory on the remote hosts
log_dir = "~/miner_github/analyzer/logs/"
# Time threshold in minutes
time_threshold = 25








def get_ssh_client(host):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host)
    return client

def get_latest_log_entry(client):
    stdin, stdout, stderr = client.exec_command(f"cd {log_dir} && tail -n 1 $(ls -t | head -1)")
    latest_log = stdout.read().decode().strip()
    return latest_log

def get_current_time(client):
    stdin, stdout, stderr = client.exec_command("date +'%Y-%m-%d %H:%M:%S'")
    current_time = stdout.read().decode().strip()
    return current_time

def kill_script(client):
    client.exec_command(f"kill -9 $(pgrep -f '{script_to_kill}')")

def update_csv(client):
    client.exec_command(f"python /miner_github/update_state.py')")
    
def check_logs(host):
    client = get_ssh_client(host)
    print(f"Checking logs for host: {host}")

    latest_log = get_latest_log_entry(client)
    print(f"Latest log entry: {latest_log}")

    if not latest_log:
        print(f"No log entry found for host: {host}")
        client.close()
        return

    log_time_str = " ".join(latest_log.split()[:2]).replace(",", ".")
    log_time = datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S.%f")
    print(f"Extracted log time: {log_time}")

    current_time_str = get_current_time(client)
    current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S")
    print(f"Current time on host: {current_time}")

    time_diff = (current_time - log_time).total_seconds() / 60
    print(f"Time difference: {time_diff} minutes")

    if time_diff > time_threshold:
        print(f"Time difference exceeds threshold. Killing the script on {host}.")
        print(f"First updating csv!")
        update_csv(client)
        print(f"Now killing")
        kill_script(client)
    else:
        print(f"Time difference is within the threshold.")

    client.close()

def main():
    with open(hosts_file, 'r') as file:
        hosts = [line.strip() for line in file.readlines() if line.strip()]

    if not hosts:
        print("Error: The hosts file is either missing or empty.")
        return

    print("Hosts file content:")
    print("\n".join(hosts))

    while True:
        for host in hosts:
            check_logs(host)
        # Wait for a specified interval before checking again (e.g., 5 minutes)
        time.sleep(400)

if __name__ == "__main__":
    main()