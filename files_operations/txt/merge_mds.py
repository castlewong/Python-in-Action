# MERGE MULTIPLE MD FILES INSIDE ONE FOLDER INTO ONE MD FILE.

import os

def combine_md_files(folder_path, output_file_name):
    # Get a list of all .md files in the folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

    # Sort the files alphabetically (optional)
    md_files.sort()

    # Create the full path for the output file
    output_file_path = os.path.join(folder_path, output_file_name)

    # Open the output file in write mode
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        # Iterate through each file in the folder
        for md_file in md_files:
            file_path = os.path.join(folder_path, md_file)
            # Open and read the content of each .md file
            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                # Write the content to the output file
                outfile.write(content)
                outfile.write("\n\n")  # Add a blank line between files (optional)

    print(f"Combined {len(md_files)} Markdown files into {output_file_path}")


if __name__ == "__main__":
    folder_path = '/Users/wilburwong/Library/CloudStorage/Dropbox/Obsidian itself/1 Olympic Cost/'  # Change to your folder path
    output_file_name = 'combined_output2.md'  # The output file name
    combine_md_files(folder_path, output_file_name)
