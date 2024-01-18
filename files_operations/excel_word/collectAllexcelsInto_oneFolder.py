import os
import shutil

# Specify the root folder containing subfolders with Excel files
root_folder = '/Users/wilburwong'

# Specify the destination folder where you want to move all Excel files
destination_folder = '/Users'

# Iterate through subfolders
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        # Check if the file is an Excel file
        if filename.endswith('.xlsx'):
            # Construct the full path to the Excel file
            excel_file_path = os.path.join(foldername, filename)

            # Move the Excel file to the destination folder
            shutil.move(excel_file_path, os.path.join(destination_folder, filename))
