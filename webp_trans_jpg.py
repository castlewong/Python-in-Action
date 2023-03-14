import os
from PIL import Image

# Set the path of the folder, macOS Env
download_folder_path = "/Users/wilburwong/Downloads"

# Get a list of all the files in the Download folder
download_files = os.listdir(download_folder_path)

# Loop through each file and convert WebP files to JPG
# In case there are multiple webp files
for file in download_files:
    if file.endswith(".webp"):
        # Open the WebP image
        webp_image_path = os.path.join(download_folder_path, file)
        webp_image = Image.open(webp_image_path)

        # Convert the WebP image to JPG
        jpg_image_path = os.path.join(download_folder_path, file[:-5] + ".jpg")
        webp_image.save(jpg_image_path, "jpeg")

        # Delete the original WebP image
        os.remove(webp_image_path)

