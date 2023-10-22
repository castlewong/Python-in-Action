import pysubs2
import pandas as pd
import re


def convert_ass_to_excel(input_file, output_file):
    # Read the .ass file
    subs = pysubs2.load(input_file, encoding="utf-8")

    # Prepare data for Excel
    data = []
    for line in subs:
        # Check if the line contains Chinese characters
        if not re.search('[\u4e00-\u9fff]', line.text):
            # Convert start and end times to format "HH:MM:SS.ms"
            start_time = f"{line.start // 3600000:02d}:{(line.start // 60000) % 60:02d}:{(line.start // 1000) % 60:02d}.{line.start % 1000:03d}"
            end_time = f"{line.end // 3600000:02d}:{(line.end // 60000) % 60:02d}:{(line.end // 1000) % 60:02d}.{line.end % 1000:03d}"

            data.append({
                'Start Time': start_time,
                'End Time': end_time,
                'Subtitle': line.text
            })

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Write to Excel
    df.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Excel file created successfully: {output_file}")


def convert_ass_to_excel_chinese(input_file, output_file):
    # Read the .ass file
    subs = pysubs2.load(input_file, encoding="utf-8")

    # Prepare data for Excel
    data = []
    for line in subs:
        # Check if the line contains Chinese characters
        if re.search('[\u4e00-\u9fff]', line.text):
            # Convert start and end times to format "HH:MM:SS.ms"
            start_time = f"{line.start // 3600000:02d}:{(line.start // 60000) % 60:02d}:{(line.start // 1000) % 60:02d}.{line.start % 1000:03d}"
            end_time = f"{line.end // 3600000:02d}:{(line.end // 60000) % 60:02d}:{(line.end // 1000) % 60:02d}.{line.end % 1000:03d}"

            data.append({
                'Start Time': start_time,
                'End Time': end_time,
                'Subtitle': line.text
            })

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Write to Excel
    df.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Excel file with Chinese subtitles created successfully: {output_file}")


def merge_subtitle_excel_files(english_file, chinese_file, output_file):
    # Read the Excel files
    df_english = pd.read_excel(english_file)
    df_chinese = pd.read_excel(chinese_file)

    # Rename columns for clarity
    df_english.columns = ['Start Time', 'End Time', 'English Subtitle']
    df_chinese.columns = ['Start Time', 'End Time', 'Chinese Subtitle']

    # Merge the dataframes based on 'Start Time'
    df_merged = pd.merge(df_english, df_chinese[['Start Time', 'Chinese Subtitle']],
                         on='Start Time', how='outer')

    # Sort by Start Time
    df_merged = df_merged.sort_values('Start Time')

    # Reorder columns
    df_merged = df_merged[['Start Time', 'End Time', 'English Subtitle', 'Chinese Subtitle']]

    # Write to a new Excel file
    df_merged.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Merged Excel file created successfully: {output_file}")



# Use the function


input_file = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/House.of.Cards.S01E02.2013.BluRay.X264.AAC.en&chs.ass"
output_file = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/output-en.xlsx"
output_file_ch = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/output-ch.xlsx"

# convert_ass_to_excel(input_file, output_file)
# convert_ass_to_excel_chinese(input_file, output_file_ch)

# Use the function
english_file = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/output-en.xlsx"
chinese_file = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/output-ch.xlsx"
output_file_merge = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/output-merge03.xlsx"

merge_subtitle_excel_files(english_file, chinese_file, output_file_merge)
