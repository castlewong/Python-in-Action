import pandas as pd

# 读取 Excel 文件
excel_file_path = 'tenant.xlsx'
df = pd.read_excel(excel_file_path)

# 定义分类函数
def classify_unit_type(name):
    keywords = {
        '1': ['幼儿园', '小学', '物业管理', '家庭旅馆', '社区', '医药', '幼儿托管所'],
        '2': ['美发店', '图文店', '艺术培训学校', '旅馆', '游戏室', '电动车商行', '足浴', '宾馆' ],
        '3': ['幼儿园', '托儿所'],
        '4': ['残疾人', '养老'],
        '5': ['住宅'],
        '6': ['门窗', '房地产', '医药',
                         '学校', '幼儿园', '教育咨询', '药房', '门诊'],
        '7': ['食府', '奶茶', '小吃店', '美食', '酒店', '便利店', '茶餐厅', '餐饮', '餐馆', '火锅', '面馆', '饭店', '餐厅', '餐饮店', '咖啡'],
        '8': ['物流', '快递', '申通', '快运', '驿站', '快送', '快递公司', '快递服务', '快递公司'],
        '9': ['超市', '商行', '水果店', '生鲜', '食品', '百货店', '商行', '理发店', '服装店', '童装']
    }

    for unit_type, unit_keywords in keywords.items():
        for keyword in unit_keywords:
            if keyword in name:
                return unit_type
    return '6'


# 应用分类函数
df['分类'] = df['商户名称'].apply(classify_unit_type)

# 保存结果到新 Excel 文件
output_excel_path = 'output_classification.xlsx'
df.to_excel(output_excel_path, index=False)

print(f"分类结果已保存到 {output_excel_path}")
