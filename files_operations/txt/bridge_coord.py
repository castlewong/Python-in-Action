import re

def extract_coordinates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            # Find all floating-point numbers in the line
            numbers = re.findall(r"[-+]?\d*\.\d+", line)

            if len(numbers) >= 2:
                # Extract the second and third numbers (longitude & latitude)
                longitude, latitude = numbers[:2]
                f.write(f"{longitude},{latitude}\n")


# File paths (replace with actual paths)
input_file = "/Users/wilburwong/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/9E04D29227559CE369BF25BC68B0FF4C/Caches/Files/2025-03/9143591d17750c2410420d4a30e8d76a/桥位置.txt"
output_file = "/Users/wilburwong/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/9E04D29227559CE369BF25BC68B0FF4C/Caches/Files/2025-03/9143591d17750c2410420d4a30e8d76a/output.txt"

# Run the function
extract_coordinates(input_file, output_file)

print(f"Processed file saved as {output_file}")
