import json

def convert_to_new_structure(old_json_path, new_json_path):
    with open(old_json_path, 'r', encoding='utf-8') as old_file:
        old_data = json.load(old_file)

    new_data = []
    for word, definition in old_data.items():
        new_data.append({
            "id": len(new_data) + 1,
            "word": word,
            "definition": definition,
            "recallStatus": 1,
            "recallCount": 0
        })

    with open(new_json_path, 'w', encoding='utf-8') as new_file:
        json.dump(new_data, new_file, ensure_ascii=False, indent=2)

# Replace 'output.json' with the actual file name
old_json_path = '/Users/wilburwong/Downloads/output.json'
new_json_path = '/Users/wilburwong/Downloads/output_new.json'

convert_to_new_structure(old_json_path, new_json_path)
