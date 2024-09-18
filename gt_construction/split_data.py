import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'results_mappings_c++.csv'  # Replace with your CSV file path

# Read the CSV file
df = pd.read_csv(file_path)

# Split the dataframe into 5 equal parts
split_dfs = np.array_split(df, 5)

# Save each part as a new CSV file with the header
for i, split_df in enumerate(split_dfs):
    split_df.to_csv(f'input_part_{i+1}.csv', index=False)
