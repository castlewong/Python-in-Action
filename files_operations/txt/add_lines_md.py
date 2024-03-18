import os

def add_empty_line_to_md_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            modified_lines = []
            for line in lines:
                modified_lines.append(line.rstrip('\n'))
                if line.strip() == '':
                    modified_lines.append('\n')

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(modified_lines))

folder_path = '/Users/wilburwong/Library/CloudStorage/Dropbox/Obsidian itself/untitled'
add_empty_line_to_md_files(folder_path)
