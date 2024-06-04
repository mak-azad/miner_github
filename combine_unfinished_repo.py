import pandas as pd
import glob

# Define the path pattern to match the CSV files
path_pattern = "/home/ubuntu/tmp/partial_work/github_repositories_*.csv"

# Use glob to get a list of file paths matching the pattern
file_paths = glob.glob(path_pattern)

# Initialize an empty list to hold dataframes
dataframes = []

# Loop through the file paths and read each file
for file_path in file_paths:
    df = pd.read_csv(file_path)
    # Filter rows where the 'processed' column is False
    filtered_df = df[df['processed'] == False]
    dataframes.append(filtered_df)

# Concatenate all the filtered dataframes
combined_df = pd.concat(dataframes)

# Save the combined dataframe to a new CSV file
output_path = "combined_unprocessed_projects_latest.csv"
combined_df.to_csv(output_path, index=False)

print(f"Combined CSV file saved to {output_path}")
