import pandas as pd
import os

# Define the folder that contains all the Excel files
folder_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/气瓶/'  # Replace with your folder path

# List to hold all dataframes
dataframes = []

# Loop through all Excel files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is an Excel file (you can adjust extensions if necessary)
    if file_name.endswith('.xls') or file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)

        # Read the Excel file and append it to the list of DataFrames
        df = pd.read_excel(file_path)
        dataframes.append(df)

# Concatenate all DataFrames together (ignore index to reset row numbering)
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new Excel file
output_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/气瓶/merged_output_flask.xlsx'  # Path where you want to save the merged Excel
merged_df.to_excel(output_path, index=False)

print(f'Merged Excel file created: {output_path}')
