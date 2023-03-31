import os

folder_path = "/Users/wilburwong/Downloads/Zlibrary"

# List all files in the directory
file_list = os.listdir(folder_path)

# Iterate through each file
for file_name in file_list:
    # Check if the file has the string to be removed
    if "string-to-remove" in file_name:
        # Replace the string with an empty string
        new_file_name = file_name.replace("(Z-Library)", "")
        # Rename the file
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
