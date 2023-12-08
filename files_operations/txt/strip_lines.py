import openpyxl

# Open the text file for reading
with open('txt.txt', 'r', encoding='utf-8') as file:
    # Read all lines from the file
    lines = file.readlines()

# Remove blank lines and split each line into parts
data = [line.strip().split() for line in lines if line.strip()]

# Create a new Excel workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write the data to the Excel sheet
for row, line_parts in enumerate(data, start=1):
    for col, part in enumerate(line_parts, start=1):
        sheet.cell(row=row, column=col, value=part)

# Save the Excel file
workbook.save('line_output.xlsx')
