import json
import csv
import glob
import os

input_folder = "/Users/wilburwong/Documents/LLM/json"   # your folder
output_file = "/Users/wilburwong/Documents/LLM/json/amap2amap.csv"

all_rows = []
all_columns = set()

# Step 1: Collect all rows and columns
for file_path in glob.glob(os.path.join(input_folder, "*.json")):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Skipping invalid JSON: {file_path}")
            continue

    items = data.get("data", {}).get("items", [])
    print(f"📄 {file_path}: Found {len(items)} items")

    for item in items:
        row = {}

        # merge top-level item fields
        for k, v in item.items():
            if k != "data":
                row[k] = v
                all_columns.add(k)

        # merge nested "data" fields
        for k, v in item.get("data", {}).items():
            row[k] = v
            all_columns.add(k)

        all_rows.append(row)

# Step 2: Write to CSV
all_columns = sorted(all_columns)  # consistent column order
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=all_columns)
    writer.writeheader()
    for row in all_rows:
        writer.writerow(row)

print(f"✅ Done! Extracted {len(all_rows)} items into '{output_file}'.")
print(f"📝 Columns: {len(all_columns)} -> {all_columns}")
