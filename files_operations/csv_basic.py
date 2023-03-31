# The AttributeError you are receiving is indicating that
# there is a circular import issue with the csv module.
# To fix this error, try renaming your script to something other than csv.py.
# This is because when you attempt to import the csv module in a script called csv.py,
# Python can get confused and import the script itself instead of the csv module.
# This can cause a circular import issue.

import csv

# Read data from input CSV file
with open('input.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)
    data = [row for row in csv_reader]

# Perform data processing
processed_data = []
for row in data:
    # Do some data processing here
    processed_row = [row[0], int(row[1]) * 2]
    processed_data.append(processed_row)

# Write processed data to output CSV file
with open('output.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(processed_data)