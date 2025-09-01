import json
from pathlib import Path

# Input / Output files
input_file = Path("/Users/wilburwong/Documents/LLM/emoji_jp_words_with_name.json")
output_file = Path("/Users/wilburwong/Documents/LLM/emoji_jp_words_clean.json")

# Load JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Remove all ":" from emoji_name
for item in data:
    if "emoji_name" in item and isinstance(item["emoji_name"], str):
        item["emoji_name"] = item["emoji_name"].replace(":", "")

# Save cleaned JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cleaned JSON saved to {output_file}")
