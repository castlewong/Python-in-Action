import json
from pathlib import Path
from deep_translator import GoogleTranslator
import pykakasi

# ---------------------------
# Initialize translators
# ---------------------------
translator_ja = GoogleTranslator(source='en', target='ja')  # English → Japanese
translator_zh = GoogleTranslator(source='en', target='zh-CN')  # English → Chinese

# Initialize pykakasi for kana conversion
kks = pykakasi.kakasi()
kks.setMode("H", "a")  # Hiragana output
kks.setMode("K", "a")  # Katakana output (not needed here, but just in case)
kks.setMode("J", "a")  # Japanese input
kks.setMode("r", "Hepburn")  # Romanization if needed
kks_converter = kks.getConverter()

# ---------------------------
# Paths
# ---------------------------
input_file = Path("/Users/wilburwong/Documents/LLM/emoji_jp_words_clean_copy.json")
output_file = Path("/Users/wilburwong/Documents/LLM/emojis_with_jp_full.json")

# ---------------------------
# Load JSON
# ---------------------------
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---------------------------
# Process each emoji entry
# ---------------------------
for item in data:
    emoji_name_clean = item.get("emoji_name", "").strip(":").strip()

    if emoji_name_clean:
        # Translate to Japanese
        try:
            jp_text = translator_ja.translate(emoji_name_clean)
        except Exception as e:
            print(f"Error translating '{emoji_name_clean}' to Japanese: {e}")
            jp_text = ""

        # Convert Japanese to full kana
        try:
            kana_text = kks_converter.do(jp_text)
        except Exception as e:
            print(f"Error converting '{jp_text}' to kana: {e}")
            kana_text = ""

        # Translate to Chinese
        try:
            zh_text = translator_zh.translate(emoji_name_clean)
        except Exception as e:
            print(f"Error translating '{emoji_name_clean}' to Chinese: {e}")
            zh_text = ""
    else:
        jp_text = ""
        kana_text = ""
        zh_text = ""

    # Update JSON item
    item["jpword"] = jp_text
    item["kana"] = kana_text
    item["mean"] = zh_text
    item["sample"] = ""  # Leave sample empty for now

# ---------------------------
# Save updated JSON
# ---------------------------
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Fully processed JSON saved to {output_file}")
