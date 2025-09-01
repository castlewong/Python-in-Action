import json
from pathlib import Path
from transformers import MarianMTModel, MarianTokenizer

# Path to your local opus model
model_path = "/Users/wilburwong/Documents/LLM/opus-mt-en-jap/"   # 👈 change this
tokenizer = MarianTokenizer.from_pretrained(model_path)
model = MarianMTModel.from_pretrained(model_path)

def translate_to_japanese(text):
    """Translate English text to Japanese using local opus-mt model."""
    if not text.strip():
        return ""
    batch = tokenizer([text], return_tensors="pt", padding=True)
    gen = model.generate(**batch)
    return tokenizer.decode(gen[0], skip_special_tokens=True)

# Load your JSON file
input_file = Path("/Users/wilburwong/Documents/LLM/emoji_jp_words_with_name.json")   # 👈 change to your JSON file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract emoji names and clean them
texts_to_translate = [item.get("emoji_name", "").strip(":") for item in data]

# Translate all at once for speed
batch = tokenizer(texts_to_translate, return_tensors="pt", padding=True)
generated = model.generate(**batch)
jp_texts = [tokenizer.decode(g, skip_special_tokens=True) for g in generated]

# Update JSON with translated Japanese
for item, jp_text in zip(data, jp_texts):
    item["jpword"] = jp_text

# Save to new file
output_file = Path("/Users/wilburwong/Documents/LLM/emojis_with_jp.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Translated JSON saved to {output_file}")
