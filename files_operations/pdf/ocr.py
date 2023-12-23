from pdf2image import convert_from_path
import pytesseract
import pandas as pd
from PIL import Image

# 设置 tesseract-ocr 的路径，根据你的安装位置设置
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 从PDF中提取图像
pdf_path = 'your_pdf_file.pdf'
images = convert_from_path(pdf_path)

# 创建一个Excel写入对象
excel_writer = pd.ExcelWriter('output_excel.xlsx', engine='xlsxwriter')

# 遍历每张图片并使用OCR提取文本
for i, image in enumerate(images):
    # 将图像保存为临时文件
    temp_image_path = f'temp_image_{i}.png'
    image.save(temp_image_path)

    # 使用OCR提取文本
    text = pytesseract.image_to_string(Image.open(temp_image_path))

    # 将文本转换为DataFrame
    df = pd.read_csv(pd.compat.StringIO(text), delimiter='\t')

    # 将DataFrame写入Excel文件的不同sheet
    df.to_excel(excel_writer, sheet_name=f'Sheet_{i}', index=False)

    # 删除临时图像文件
    os.remove(temp_image_path)

# 保存Excel文件
excel_writer.save()
