from files_operations.json import json
from emoji import EMOJI_DATA   # modern replacement

def get_ios_emojis_with_names():
    """获取iOS支持的emoji及其官方英文名"""
    emoji_with_names = []
    for emj, data in EMOJI_DATA.items():
        # 官方英文描述
        clean_name = data["en"].replace("_", " ")
        # 筛选（避免太长或无效符号）
        if len(emj) <= 2 and not emj.isdigit() and emj not in ['#', '*', '©', '®', '™']:
            emoji_with_names.append({
                "emoji": emj,
                "emoji_name": clean_name
            })
    # 去重 & 排序
    unique_emojis = list({item['emoji']: item for item in emoji_with_names}.values())
    return sorted(unique_emojis, key=lambda x: x['emoji_name'])

def generate_json_template(emojis_with_names, output_file="emoji_jp_words_with_name.json"):
    """生成包含emoji、英文名和预留单词字段的JSON模板"""
    grouped_data = []
    for item in emojis_with_names:
        prefix = item['emoji_name'][0].upper() if item['emoji_name'] else "?"
        entry = {
            "emoji": item['emoji'],
            "emoji_name": item['emoji_name'],
            "prefix": prefix,
            "word": "",
            "jpword": "",
            "kana": "",
            "mean": "",
            "sample": ""
        }
        grouped_data.append(entry)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(grouped_data, f, ensure_ascii=False, indent=4)
    print(f"已生成带emoji英文名的JSON模板：{output_file}，共{len(grouped_data)}个emoji")

if __name__ == "__main__":
    emojis_with_names = get_ios_emojis_with_names()
    generate_json_template(emojis_with_names)
