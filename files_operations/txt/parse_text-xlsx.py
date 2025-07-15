import pandas as pd


def txt_to_excel(txt_path, output_path):
    data = []

    with open(txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 8:
                continue  # 跳过格式不完整的行

            type_name = parts[0].lstrip('/')  # 去掉前面的斜杠
            # 名称可能含有空格，位于第2到倒数第6之间
            name = ' '.join(parts[1:-6])
            lon = parts[-6]
            lat = parts[-5]
            field1 = parts[-4]
            field2 = parts[-3]
            field3 = parts[-2]
            comment = parts[-1]

            data.append([type_name, name, lon, lat, field1, field2, field3, comment])

    df = pd.DataFrame(data, columns=[
        '类型', '名称', '经度', '纬度', '字段1', '字段2', '字段3', '备注'
    ])

    df.to_excel(output_path, index=False)
    print(f"✅ 已保存为 Excel 文件：{output_path}")


# 示例使用
txt_to_excel(
    txt_path='/Users/wilburwong/Nutstore Files/A_Company/安康排水易积水点位TXT.txt',
    output_path='/Users/wilburwong/Nutstore Files/A_Company/output.xlsx'
)
