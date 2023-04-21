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
