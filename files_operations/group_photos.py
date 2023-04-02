import os
import shutil

# 创建两个文件夹来存放分类后的图片
os.mkdir('nef_images')
os.mkdir('jpg_images')

# 遍历images文件夹中的所有文件
for filename in os.listdir('images'):
    if filename.endswith('.NEF'):
        # 如果文件名以.nef结尾，则将其移动到nef_images文件夹中
        shutil.move(f'images/{filename}', 'nef_images')
    elif filename.endswith('.JPG'):
        # 如果文件名以.jpg结尾，则将其移动到jpg_images文件夹中
        shutil.move(f'images/{filename}', 'jpg_images')
