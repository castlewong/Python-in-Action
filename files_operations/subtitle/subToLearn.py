import re

def parse_ass_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()

    dialogue_lines = [line for line in lines if line.startswith("Dialogue:")]

    subtitles = {}
    for line in dialogue_lines:
        parts = line.strip().split(",", 9)
        if len(parts) < 10:
            continue
        start_time, end_time, text = parts[1], parts[2], parts[9]
        # Clean formatting codes like {\fad(300,0)}
        text = re.sub(r"{.*?}", "", text).strip()

        key = f"{start_time} --> {end_time}"
        if key not in subtitles:
            subtitles[key] = []
        subtitles[key].append(text)

    return subtitles


def write_merged_subtitles(subtitles, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for time_range, texts in subtitles.items():
            f.write(f"[{time_range}]\n")
            for text in texts:
                f.write(text + "\n")
            f.write("\n")


if __name__ == "__main__":
    ass_path = "/Users/wilburwong/Downloads/[SweetSub]_CITY_THE_ANIMATION_01_merged.ass"  # 改成你的 .ass 文件路径
    output_path = "merged_subtitles.txt"

    subs = parse_ass_file(ass_path)
    write_merged_subtitles(subs, output_path)
    print(f"✅ 已保存到 {output_path}")
