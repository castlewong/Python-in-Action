import os

def extract_part(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    parts = []
    empty_line_count = 0

    for line in lines:
        if line.strip() == "":
            empty_line_count += 1
            if empty_line_count == 2:
                break
        else:
            if empty_line_count == 1:
                parts.append(line)
                parts.append("\n")  # Add an empty line after each non-empty line

    return ''.join(parts)

def combine_text_files(folder_path, output_file):
    with open(output_file, 'w') as f_out:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.txt'):
                input_file = os.path.join(folder_path, file_name)
                extracted_part = extract_part(input_file)
                f_out.write(extracted_part)

if __name__ == "__main__":
    folder_path = "txt"  # Replace with the path to your folder containing txt files
    output_file = "combined_output.txt"   # Name of the output file

    combine_text_files(folder_path, output_file)

# Certainly! Let me explain each part of the code step by step:
#
# 1. `for line in lines:`:
#    - This line initiates a loop
#    that iterates through each line in the `lines` list. In this context, `lines` contains all the lines from the text file.
#
# 2. `if line.strip() == "":`
#    - This checks whether the current line is
#    an empty line. The `strip()` method removes any leading or trailing whitespace (spaces, tabs, newlines) from the line, so `line.strip() == ""` evaluates to True if the line is empty.
#
# 3. `empty_line_count += 1`:
#    - If an empty line is found, the `empty_line_count`
#    variable is incremented by 1. This variable keeps track of how many consecutive empty lines have been encountered.
#
# 4. `if empty_line_count == 2:`
#    - This is a nested condition inside
#    the previous `if` block. It checks if two consecutive empty lines have been encountered. If this condition is true, it means that we have reached the end of the second part that we want to extract, so the loop is broken using `break`.
#
# 5. `else:`
#    - If the current line is not empty, this part of the code will be executed.
#
# 6. `if empty_line_count == 1:`
#    - This checks if only one empty line has been encountered so far. If this condition is true, it means that the loop has passed one empty line, and we are now inside the second part that we want to extract.
#
# 7. `parts.append(line)`:
#    - If the above condition is true, this line adds the non-empty line to the `parts` list. This list is used to store all the lines of the second part of the text.
#
# The purpose of this code is to find the second part in a text file separated by two consecutive empty lines. It extracts the lines between the first and second empty lines, which corresponds to the second part of the text. The `parts` list will contain all the lines from the second part, which will be joined together using `''.join(parts)` later in the code and returned as the output of the `extract_part` function.