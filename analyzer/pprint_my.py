import json

# Path to your .jsonl file
jsonl_file_path = 'github_repo_analysis_result_03072024_150.136.33.41_perf.jsonl'

with open(jsonl_file_path, 'r') as file:
    for line in file:
        # Parse the JSON line
        record = json.loads(line)

        # Extract method_src_before and method_src_after
        method_src_before = record.get("method_src_before", "No method_src_before data")
        method_src_after = record.get("method_src_after", "No method_src_after data")

        # Print the method source code before the change
        print("Method Source (Before):")
        print("--------------------------------------------------")
        print(method_src_before)
        print("\n")

        # Print the method source code after the change
        print("Method Source (After):")
        print("--------------------------------------------------")
        print(method_src_after)
        print("\n")
