
import csv

# 定义输入和输出文件路径
input_file = '/Users/wilburwong/Documents/Untitled.txt'  # 替换为你的文本文件路径
output_file = '/Users/wilburwong/Documents/coor_water_environ_output.csv'  # 替换为你想保存的 CSV 文件路径

# 读取文本文件内容
with open(input_file, 'r') as file:
    data = file.read()

# 将文本分割成坐标对，并去掉多余的空格
coordinates = data.split()

# 创建并写入 CSV 文件
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # 遍历每个坐标对
    for coordinate in coordinates:
        # 分割每个坐标对为经度和纬度
        longitude, latitude = coordinate.split(',')
        # 写入到 CSV 文件中
        csv_writer.writerow([longitude, latitude])

print(f"转换完成，已保存为 {output_file}")





