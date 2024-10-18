import pysubs2
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import re

def process_subtitle_file(input_file, output_file):
    # 读取 .ass 文件
    subs = pysubs2.load(input_file, encoding="utf-8")

    # 提取中英文文本
    texts = []
    for line in subs:
        text = line.text
        # 使用正则表达式来判断文本是中文还是英文
        if re.search('[\u4e00-\u9fff]', text):
            texts.append([text, ""])  # 中文在左列
        else:
            texts.append(["", text])  # 英文在右列

    # 创建 PDF
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    elements = []

    # 创建表格
    table = Table(texts, colWidths=[250, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)
    doc.build(elements)

# 使用函数
input_file = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/House.of.Cards.S01E01.2013.BluRay.X264.AAC.en&chs.ass"
output_file = "/Users/wilburwong/Downloads/[紙牌屋].House.of.Cards.S01.2013.en&amp;cht&amp;chs.yyets.rar/output.pdf"
process_subtitle_file(input_file, output_file)