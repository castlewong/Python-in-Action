import json

def simplify_json(input_file, output_file):
    simplified_data_list = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line)
                simplified_data = {
                    "wordId": data["content"]["word"]["wordId"],
                    "headWord": data["headWord"],
                    "translation": data["content"]["word"]["trans"][0]["tranCn"]
                }
                simplified_data_list.append(simplified_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except KeyError as e:
                print(f"Error extracting data: {e}")

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(simplified_data_list, file, ensure_ascii=False, indent=2)


# Example usage
input_file_path = '/Users/wilburwong/Documents/SwiftUI-Tutorials/TrySomeThing/_Examples/FlashCards-main/FlashCards/IELTS/IELTS copy.json'
output_file_path = 'vocabulary_output.json'

simplify_json(input_file_path, output_file_path)
