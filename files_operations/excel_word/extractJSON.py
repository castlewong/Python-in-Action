
import pandas as pd
import json
import os

file_path = '/Users/wilburwong/Desktop/json.xlsx'
df = pd.read_excel(file_path)

json_column = 'extra_field'

def expand_json(row):
    try:
        json_data = json.loads(row[json_column])
        return pd.Series(json_data)
    except json.JSONDecodeError:
        return pd.Series()

expanded_columns = df.apply(expand_json, axis=1)
df = pd.concat([df, expanded_columns], axis=1)

# output_file_path = 'json_new.xlsx'
# 设置输出文件夹和文件名
output_folder = '你的输出文件夹路径'  # 替换为你想要的文件夹路径
output_filename = 'output_file.xlsx'  # 设置输出文件名
output_file_path = os.path.join(output_folder, output_filename)

df.to_excel(output_file_path, index=False)

print(f'数据已成功保存到 {output_file_path}')
