import os

# Define the folder that contains all the .docx files
folder_path = '/Users/wilburwong/Nutstore Files/'  # Replace with the path to your folder

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a .docx file and starts with 'aaatt'
    if file_name.endswith('.docx') and file_name.startswith('aaa'):
        # Define the new file name by replacing 'aaatt' with 'bbbtt'
        new_file_name = file_name.replace('aaa', 'bb', 1)

        # Construct full file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

        print(f'Renamed: {file_name} -> {new_file_name}')

print('All files have been renamed.')
