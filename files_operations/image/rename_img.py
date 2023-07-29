import os

# Specify the path to the folder containing the images
folder_path = "./article"

# List all files in the folder
files = os.listdir(folder_path)

# Define the desired new prefix for the filenames
new_prefix = "article"

# Initialize a counter
counter = 1

# Loop through the files and rename them
for file in files:
    # Check if the file is an image (e.g., .jpg, .png, etc.)
    if file.lower().endswith((".jpg", ".png", ".jpeg", ".gif")):
        # Construct the new filename
        new_filename = os.path.join(folder_path, f"{new_prefix}{counter}.jpg")

        # Get the full path of the current file
        current_filepath = os.path.join(folder_path, file)

        # Rename the file
        os.rename(current_filepath, new_filename)

        # Increment the counter
        counter += 1

print("Images renamed successfully.")
