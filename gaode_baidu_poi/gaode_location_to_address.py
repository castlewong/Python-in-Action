# 根据 Excel 文件中的经纬度数据列找对应的地址文字信息
# 误差大约 200 米内，勉强能用

import pandas as pd
import requests

# 读取 Excel 文件
file_name = 'your_file_name.xls'
df = pd.read_excel(file_name)

# 选择经度和纬度列

lng_column = 'longitude'
lat_column = 'latitude'

# 构建高德地图 API 的请求 URL
url = 'https://restapi.amap.com/v3/geocode/regeo'
key = 'd89a69807995de229a156eaad31b796b'
params = {
    'key': key,
    'output': 'json',
    'location': None,
}
results = []

# 遍历 DataFrame 中的每一行
for index, row in df.iterrows():
    # 获取经纬度坐标
    lng = row[lng_column]
    lat = row[lat_column]

    # 构建请求 URL，并发送请求
    params['location'] = f'{lng},{lat}'  # 格式：经度,纬度
    response = requests.get(url, params=params)

    # 解析响应
    try:
        result = response.json()['regeocode']['formatted_address']
    except:
        result = 'Error'

    # 保存结果
    results.append(result)

# 将结果添加到 DataFrame 中
df['address'] = results

# 把修改后的 DataFrame 保存为新的 Excel 文件
new_file_name = 'new_file_name.xlsx'
df.to_excel(new_file_name, index=False)
