import json

# Load the original JSON
with open("/Users/wilburwong/Documents/LLM/emojis_with_jp_full.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Define skin tone phrases to filter out
skin_tones = [
    "light skin tone",
    "medium-light skin tone",
    "medium skin tone",
    "medium-dark skin tone",
    "dark skin tone"
]

# Filter JSON: keep only items NOT containing these substrings
filtered_data = [
    item for item in data
    if not any(tone in item.get("emoji_name", "").lower() for tone in skin_tones)
]

# Save the filtered JSON
with open("/Users/wilburwong/Documents/LLM/emojis_filtered.json", "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print(f"Original count: {len(data)}")
print(f"Filtered count: {len(filtered_data)}")
