import pandas as pd
import re

# Read the input Excel file, assuming the data is in the sheet named 'Sheet1'
df = pd.read_excel("/Users/wilburwong/Documents/Python-in-Action/your_excel_file.xls", sheet_name="Sheet1")

# Define a function to convert DMS coordinates to decimal format
def dms2dd(dms):
    '''
    Convert degrees-minutes-seconds coordinate format to decimal format.
    Parameters:
    dms - degrees-minutes-seconds coordinate string, e.g. "40°26'46.5\"N"
    Returns:
    dd - decimal coordinate format, e.g. 40.44625
    '''
    # Use regular expression to extract degrees, minutes, and seconds
    parts = re.split('[°\'"]', dms)
    # Convert degrees, minutes, and seconds to floating-point numbers
    d = float(parts[0])
    m = float(parts[1])
    s = float(parts[2])
    # Convert to decimal format
    dd = d + m/60 + s/3600
    # Check if the coordinate is in the southern or western hemisphere
    if parts[-1] in ['S', 'W']:
        dd = -dd
    return dd

# Convert latitude and longitude to decimal format
df['Latitude'] = df['X2'].apply(dms2dd)
df['Longitude'] = df['Y2'].apply(dms2dd)

# Write the output to a new Excel file
writer = pd.ExcelWriter('output_file.xls')
df.to_excel(writer, index=False, sheet_name='Sheet1')
writer.save()

print('Output saved to output_file.xls.')
