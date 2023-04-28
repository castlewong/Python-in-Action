import pandas as pd
import os

# Replace with the path to your directory containing the Excel files
directory = "/Users/wilburwong/Documents/Python-in-Action/files_operations/xlsx_word/xlsx-to-combline"

# List all Excel files in the directory
excel_files = [f for f in os.listdir(directory) if f.endswith(".xlsx")]

# Create a Pandas Excel writer using xlsxwriter as an engine
writer = pd.ExcelWriter("combined.xlsx", engine="xlsxwriter")

# Loop through each Excel file and read it into a Pandas dataframe
for filename in excel_files:
    sheetname = os.path.splitext(filename)[0] # Get sheetname from filename
    df = pd.read_excel(os.path.join(directory, filename), sheet_name=sheetname)

    # Write the dataframe to a new sheet in the output Excel file
    df.to_excel(writer, sheet_name=sheetname, index=False)

# Save the output Excel file
writer.save()

print("All Excel files combined successfully!")
