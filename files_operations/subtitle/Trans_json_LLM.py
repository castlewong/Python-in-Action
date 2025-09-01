import json
from pathlib import Path
import ollama

def translate_with_llm(text):
    """Translate English text to Japanese (short word/phrase only)."""
    if not text.strip():
        return ""

    # Clean instruction to return only the Japanese word/phrase
    prompt = f"""
Translate this English word or phrase into Japanese.
Return ONLY the Japanese word or short phrase. No English, no punctuation, no explanations.
{text}
"""

    # Call Ollama chat API
    response = ollama.chat(
        model="gemma:2b",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract response text safely
    if isinstance(response, dict):
        if "message" in response and isinstance(response["message"], dict):
            return response["message"].get("content", "").strip()
        return response.get("content", "").strip()
    else:
        return str(response).strip()


# ---- Main workflow ----
input_file = Path("/Users/wilburwong/Documents/LLM/emoji_jp_words_clean.json")
output_file = Path("/Users/wilburwong/Documents/LLM/emojis_with_jp.json")

# Load JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Translate each entry
for item in data:
    en_text = item.get("emoji_name", "").strip(":").strip()  # remove ":" and extra spaces
    jp_text = translate_with_llm(en_text)
    item["jpword"] = jp_text

# Save new JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Translated JSON saved to {output_file}")
