# import pandas as pd
#
#
# def get_distinct_values(excel_path, column_name):
#     # Load the Excel file into a pandas DataFrame
#     df = pd.read_excel(excel_path)
#
#     # Get distinct (unique) values from the specified column
#     distinct_values = df[column_name].dropna().unique()
#
#     return distinct_values
#
#
# # Example usage
# excel_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/updated-merged_output_flask-after-join.xlsx'  # Replace with your actual file path
# column_name = 'org_id'  # Replace with the actual column name you want to extract distinct values from
#
# distinct_values = get_distinct_values(excel_file_path, column_name)
#
# # Print the distinct values
# print(distinct_values)

import pandas as pd
import re

def is_chinese(string):
    """Check if the string contains Chinese characters."""
    for ch in string:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def get_distinct_values_and_group_chinese(excel_path, column_name):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_path)

    # Get distinct (unique) values from the specified column, excluding NaNs
    distinct_values = df[column_name].dropna().unique()

    # Separate values with Chinese characters and non-Chinese values
    chinese_values = [val for val in distinct_values if is_chinese(str(val))]
    non_chinese_values = [val for val in distinct_values if not is_chinese(str(val))]

    return chinese_values, non_chinese_values

def save_values_to_file(chinese_values, non_chinese_values, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as f:
        # Write Chinese values first
        f.write("Chinese Values:\n")
        for val in chinese_values:
            f.write(f"{val}\n")

        # Add a separator line
        f.write("\nNon-Chinese Values:\n")

        # Write non-Chinese values
        for val in non_chinese_values:
            f.write(f"{val}\n")


# Example usage
excel_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/updated-merged_output_flask-after-join-appedTEXT.xlsx'  # Replace with your actual file path
column_name = 'station_id'  # Replace with the actual column name
output_file = '../excel/distinct_values_output-station.txt'  # Output text file to save the result

chinese_values, non_chinese_values = get_distinct_values_and_group_chinese(excel_file_path, column_name)
save_values_to_file(chinese_values, non_chinese_values, output_file)

print(f"Distinct values saved to {output_file}")
