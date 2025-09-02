import json
import glob
import os

input_folder = "/Users/wilburwong/Documents/LLM/json/"   # change this to your folder

for file_path in glob.glob(os.path.join(input_folder, "*.json")):
    print(f"\n🔍 Checking {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Invalid JSON file")
            continue

    # Show top-level keys
    print("Top-level keys:", list(data.keys())[:10])

    # Show if "data" and "items" exist
    if "data" in data:
        print("✅ Found 'data'")
        if "items" in data["data"]:
            print(f"✅ Found {len(data['data']['items'])} items")
        else:
            print("⚠️ No 'items' key inside 'data'")
    elif "items" in data:
        print(f"✅ Found {len(data['items'])} items at top-level")
    else:
        print("⚠️ No 'items' found anywhere")
