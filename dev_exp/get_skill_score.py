import pandas as pd
import numpy as np


def aggregate_domain_vectors_with_pandas_f1(filepath, output_excel_path):
    # Load the entire JSONL file into a DataFrame, ensuring domain_vec is treated as a string
    df = pd.read_json(filepath, lines=True, dtype={'domain_vec': str, 'pred': str})

    # Filter the DataFrame to include only rows where 'pred' is '0'
    df = df[df['pred'] == '1']

    # Apply a transformation to convert each 'domain_vec' string into a list of integers
    domain_vectors = df['domain_vec'].apply(lambda x: [int(char) for char in x])

    # Create a new DataFrame from the list of lists, where each inner list becomes a row
    domain_df = pd.DataFrame(domain_vectors.tolist(), index=df.index)
    domain_df.columns = [f'cat_{i+1}' for i in range(domain_df.shape[1])]

    # Add 'dev_email' back to the new DataFrame for grouping
    domain_df['dev_email'] = df['dev_email']

    # Aggregate the domain vectors by email, summing up each corresponding position in the vectors
    aggregated = domain_df.groupby('dev_email').sum()
    
    
    # Calculate the sum of all categories for each author and add it as a new column 'sum'
    aggregated['sum'] = aggregated.sum(axis=1)
    aggregated['avg_sum'] = aggregated['sum'] / 14
    aggregated['log_normalized_avg'] = np.log(aggregated['avg_sum'] + 1)

    # Save the DataFrame to an Excel file directly, preserving the separate columns for each category
    aggregated.to_excel(output_excel_path, sheet_name='Aggregated_Vectors')

    return aggregated


def aggregate_domain_vectors_with_pandas(filepath, output_excel_path):
    # Load the entire JSONL file into a DataFrame, ensuring domain_vec is treated as a string
    df = pd.read_json(filepath, lines=True, dtype={'domain_vec': str})

    # Apply a transformation to convert each 'domain_vec' string into a list of integers
    domain_vectors = df['domain_vec'].apply(lambda x: [int(char) for char in x])

    # Create a new DataFrame from the list of lists, where each inner list becomes a row
    domain_df = pd.DataFrame(domain_vectors.tolist(), index=df.index)
    domain_df.columns = [f'cat_{i+1}' for i in range(domain_df.shape[1])]

    # Add 'dev_email' back to the new DataFrame for grouping
    domain_df['dev_email'] = df['dev_email']

    # Aggregate the domain vectors by email, summing up each corresponding position in the vectors
    aggregated = domain_df.groupby('dev_email').sum()
    
    # Calculate the sum of all categories for each author and add it as a new column 'sum'
    aggregated['sum'] = aggregated.sum(axis=1)
    aggregated['avg_sum'] = aggregated['sum'] / 14
    aggregated['log_normalized_avg'] = np.log(aggregated['avg_sum'] + 1)

    # Save the DataFrame to an Excel file directly, preserving the separate columns for each category
    aggregated.to_excel(output_excel_path, sheet_name='Aggregated_Vectors')

    return aggregated

# Example usage (assuming the file path to your JSONL file is correct)
file_path = 'hardcoded_data.jsonl'  # Ensure this path is correct
output_excel_path = 'Aggregated_Domain_Vectors_1.xlsx'
result = aggregate_domain_vectors_with_pandas(file_path, output_excel_path)
print("Results have been written to Excel:", output_excel_path)