import os
import json
import oci
from oci.object_storage import ObjectStorageClient
import socket

def get_oci_config():
    """
    Load the OCI configuration. Modify this function if you need to load a specific profile.
    """
    return oci.config.from_file()

def upload_file_to_object_storage(namespace, bucket_name, object_name, file_path, oci_config):
    """
    Uploads a file to Oracle Cloud Infrastructure Object Storage using streaming and deletes the file afterwards.
    """
    object_storage_client = ObjectStorageClient(oci_config)
    with open(file_path, 'rb') as file:
        object_storage_client.put_object(namespace, bucket_name, object_name, file)
        print(f"Upload completed: {object_name}")
    
    # Remove the file after successful upload
    try:
        os.remove(file_path)
        print(f"Successfully deleted local file: {file_path}")
    except OSError as e:
        print(f"Error deleting file {file_path}: {e}")

def write_commit_data_to_file_and_upload(namespace, bucket_name, commit_data, results_dir, batch_id):
    """
    Writes commit data to a .jsonl file, uploads it to OCI Object Storage, and removes the file locally.
    """
    hostname = socket.gethostname()
    filename = f"{hostname}_test2_batch_{batch_id}.jsonl"
    file_path = os.path.join(results_dir, filename)
    
    try:
        with open(file_path, 'w') as file:
            for commit_info in commit_data:
                file.write(json.dumps(commit_info) + '\n')
        
        oci_config = get_oci_config()  # Load the OCI configuration
        upload_file_to_object_storage(namespace, bucket_name, filename, file_path, oci_config)
    except IOError as e:
        print(f"An error occurred while writing or uploading the file: {e}")
    finally:
        commit_data.clear()
          
# Example usage
if __name__ == "__main__":
    namespace = 'idqgqghww6tn'
    bucket_name = 'bucket-20240402-1601'
    #commit_data = []  # Assume this is populated with your data
    # Example data
    commit_data = [{'id': 1, 'message': 'First commit'}, {'id': 2, 'message': 'Second commit'}]
    results_dir = '.'
    batch_id = 1
    
    write_commit_data_to_file_and_upload(namespace, bucket_name, commit_data, results_dir, batch_id)
