import pandas as pd

# 读取chao.xls文件
df_chao = pd.read_excel('/Users/wilburwong/bei.xls')

# 读取goal.xls文件
df_goal = pd.read_excel('/Users/wilburwong/goal.xls')

# 合并两个DataFrame，使用设备名称作为标识符
df_merged = pd.merge(df_goal, df_chao[['ID', '经度', '纬度', '高度']], on='ID')

# 将合并后的DataFrame保存为新的xls文件
df_merged.to_excel('/Users/wilburwong/Documents/result_bei.xls', index=False)
