import tkinter as tk
from tkinter import filedialog
from PIL import Image

def split_image():
    # Ask user to select an image file
    file_path = filedialog.askopenfilename(title="Select Image File")

    # Load the image
    image = Image.open(file_path)

    # Get the dimensions of the image
    width, height = image.size

    # Split the image into 4 equal parts
    part_width = width // 2
    part_height = height // 2

    parts = []
    for i in range(2):
        for j in range(2):
            # Crop each part of the image
            left = i * part_width
            top = j * part_height
            right = left + part_width
            bottom = top + part_height
            part = image.crop((left, top, right, bottom))
            parts.append(part)

    # Save each part of the image
    for i, part in enumerate(parts):
        part.save(f"part{i+1}.png")

    # Display a success message
    result_label.config(text="Image split into parts successfully.")

# Create the main application window
window = tk.Tk()
window.title("Image Splitter")

# Create a button to trigger the image splitting
split_button = tk.Button(window, text="Split Image", command=split_image)
split_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main application loop
window.mainloop()
