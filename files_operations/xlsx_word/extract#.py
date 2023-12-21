# import pandas as pd
#
# # Load the Excel file into a pandas DataFrame
# excel_file_path = 'xiang.xlsx'
# df = pd.read_excel(excel_file_path)
#
# # Extract the value after '#' in the "address" column
# df['new_column'] = df['address'].str.extract(r'#(.*)')
#
# # Save the modified DataFrame back to a new Excel file
# output_excel_path = 'output_xiang.xlsx'
# df.to_excel(output_excel_path, index=False)
import pandas as pd

# Load the Excel file into a pandas DataFrame
excel_file_path = 'xiang.xlsx'
df = pd.read_excel(excel_file_path)

# Extract the value after '#' in the "address" column and create a new column
df['new_column'] = df['address'].str.extract(r'#(.*)')

# Remove the '#...' part from the "address" column
df['address'] = df['address'].replace(regex=r'#.*', value='')

# Save the modified DataFrame back to a new Excel file
output_excel_path = 'output_xiang.xlsx'
df.to_excel(output_excel_path, index=False)
