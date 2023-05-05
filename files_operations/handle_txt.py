import os

def extract_text_from_folder(folder_path, output_file):
    with open(output_file, "w") as outfile:
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                with open(os.path.join(folder_path, filename), "r") as infile:
                    outfile.write(infile.read())

extract_text_from_folder("txt", "output-Bookmark.txt")