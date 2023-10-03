
import re
import json

def read_txt_to_dict(file_path):
    result_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                parts = re.split(r'\s+', line, maxsplit=1)
                if len(parts) == 2:
                    word, definition = parts
                    result_dict[word] = definition.strip()
    return result_dict

def write_dict_to_json(dictionary, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(dictionary, json_file, ensure_ascii=False, indent=2)

# Replace 'your_input_file.txt' and 'output_file.json' with your actual file paths
txt_file_path = '/Users/wilburwong/Downloads/SAT.txt'
json_file_path = '/Users/wilburwong/Downloads/output.json'

words_dict = read_txt_to_dict(txt_file_path)
write_dict_to_json(words_dict, json_file_path)

# format_to_json('/Users/wilburwong/Downloads/SAT.txt', '/Users/wilburwong/Downloads/output.json')

