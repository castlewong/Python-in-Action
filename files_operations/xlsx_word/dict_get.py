

# import docx
#
# # 打开 Word 文档
# doc = docx.Document('dict.docx')
#
# # 获取第一个表格
# table = doc.tables[1]
#
# # 遍历表格中的每一行和每一列，并打印单元格中的内容
# for i, row in enumerate(table.rows):
#     text = (cell.text for cell in row.cells)
#     print(f"Row {i}: {' | '.join(text)}")

# import docx
# from openpyxl import Workbook
#
# # 打开Word文档
# doc = docx.Document('dict.docx')
#
# # 创建一个新的Excel工作簿
# wb = Workbook()
# ws = wb.active
#
# # 遍历文档中的所有段落
# for para in doc.paragraphs:
#     # 如果段落包含“字典”，则将其添加到Excel表格中
#     if '字典' in para.text:
#         ws.append([para.text])
#
# # 保存Excel文件
# wb.save('output.xlsx')
