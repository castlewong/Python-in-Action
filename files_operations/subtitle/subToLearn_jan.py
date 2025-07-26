import re

def is_japanese(text):
    """只保留含有假名的文本，更准确判断日语字幕"""
    return bool(re.search(r"[\u3040-\u309f\u30a0-\u30ff]", text))

def parse_ass_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    dialogue_lines = [line for line in lines if line.startswith("Dialogue:")]

    subtitles = {}
    jp_subtitles = {}  # 用于保存日语字幕

    for line in dialogue_lines:
        parts = line.strip().split(",", 9)
        if len(parts) < 10:
            continue
        start_time, end_time, text = parts[1], parts[2], parts[9]
        text = re.sub(r"{.*?}", "", text).strip()

        key = f"{start_time} --> {end_time}"
        if key not in subtitles:
            subtitles[key] = []
        subtitles[key].append(text)

        # 更精准地判断是否为日语（包含假名）
        if is_japanese(text):
            if key not in jp_subtitles:
                jp_subtitles[key] = []
            jp_subtitles[key].append(text)

    return subtitles, jp_subtitles

def write_merged_subtitles(subtitles, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for time_range, texts in subtitles.items():
            f.write(f"[{time_range}]\n")
            for text in texts:
                f.write(text + "\n")
            f.write("\n")

if __name__ == "__main__":
    ass_path = "/Users/wilburwong/Downloads/[SweetSub]_CITY_THE_ANIMATION_01_merged.ass"
    output_path_jp = "japanese_only.txt"

    _, jp_subs = parse_ass_file(ass_path)
    write_merged_subtitles(jp_subs, output_path_jp)

    print(f"✅ 日语字幕已保存到 {output_path_jp}")
