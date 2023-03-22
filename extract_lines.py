# extract special lines from files
#
#
# import csv
#
# # 打开源文件
# with open('/Users/wilburwong/Documents/Python-in-Action/1.sql', 'r') as f:
#     content = f.readlines()
#
# # 打开目标文件
# with open('output_file.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     # 写入表头
#     writer.writerow(['table_name', 'comment'])
#     # 遍历每一行
#     for line in content:
#         if line.startswith('COMMENT ON TABLE'):
#             # 获取表名
#             table_name = line.split()[3]
#             # 获取注释
#             comment = line.split("'")[1]
#             # 写入CSV文件
#             writer.writerow([table_name, comment])
#
# print('Extracted comments to output_file.csv')

import csv
from openpyxl import Workbook

# 打开源文件
with open('/Users/wilburwong/Documents/Python-in-Action/1.sql', 'r') as f:
    content = f.readlines()

# 创建Excel工作簿
wb = Workbook()
ws = wb.active
ws.title = "表注释"

# 写入表头
ws.append(['表名', '注释'])

# 遍历每一行
for line in content:
    if line.startswith('COMMENT ON TABLE'):
        # 获取表名
        table_name = line.split()[3]
        # 获取注释
        comment = line.split("'")[1]
        # 写入Excel文件
        ws.append([table_name, comment])

# 保存Excel文件
wb.save('output_file.xlsx')
print('输出Excel文件完成')
