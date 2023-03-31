# Transfer PNGs to PDFs
# TODO 1.Replace the directory with your own directory for storing the original files
# TODO 2.Change the output_path to your own directory for storing the PDF files

from PIL import Image
import os
def pngs_to_pdf(directory, output_path):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                # convert the image to RGB without alpha channel
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])  # 3 is the alpha channel

                images.append(rgb_img)

    images[0].save(output_path, save_all=True, append_images=images[1:])
pngs_to_pdf('/Users/wilburwong/Downloads', '/files_operations/pdf/output.pdf')
