# In summary, the code reads data from "some.txt",
# processes each line,
# and writes the formatted data to "formatted.txt".
# The processed data consists of three columns separated by tabs:
# phrase, code, and num.
# The code assumes that the lines in "some.txt"
# have a specific format,
# with each line containing a phrase and a code separated by "=",
# and optionally followed by a number separated by ",".

with open('some.txt', 'r') as f:
    lines = f.readlines()

formatted_lines = []
for line in lines:
    parts = line.strip().split('=')
    if len(parts) >= 2:
        code, phrase = parts[0].split(',')[0], parts[1]
        num = parts[0].split(',')[1] if len(parts[0].split(',')) > 1 else ''
        formatted_line = f"{phrase}\t{code}\t{num}\n"
        formatted_lines.append(formatted_line)

with open('formatted.txt', 'w') as f:
    f.write("a\tb\tc\n")
    f.writelines(formatted_lines)
