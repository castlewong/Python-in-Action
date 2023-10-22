
import pandas as pd

# Load the Excel file
# file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/enterprise_id_dict.xlsx'  # Replace with your file path
# df = pd.read_excel(file_path)
#
# # Create a new column 'id' to store enterpriseid corresponding to the enterprise name
# df['id'] = df.apply(lambda row: row['enterpriseid'] if row['enterprise'] == row['enterprisename'] else None, axis=1)
#
# # Alternatively, if you want to map directly using the 1st column to the 2nd and 3rd columns as a dictionary:
# # Create a dictionary of enterprise names and ids
# enterprise_dict = dict(zip(df['enterprisename'], df['enterpriseid']))
#
# # Assign the new 'id' column values by looking up the enterprise names in the dictionary
# df['id'] = df['enterprise'].map(enterprise_dict)
#
# # Rearrange the columns so that 'id' appears first if you need
# df = df[['id', 'enterprise', 'enterpriseid', 'enterprisename']]
#
# # Save the updated DataFrame to a new Excel file
# new_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/VLOOKUP-output.xlsx'  # Replace with your file path
# df.to_excel(new_file_path, index=False)
#
# print(f"New Excel file with ID column created: {new_file_path}")


# Load the Excel files
org_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/气瓶2/updated-merged_output_flask-after-join-staion1025.xlsx'  # Replace with your file path
dict_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/气瓶2/enterprise_station_dict.xlsx'  # Replace with your file path

org_df = pd.read_excel(org_file_path)
dict_df = pd.read_excel(dict_file_path)

org_df['station_name'] = org_df['station_name'].str.strip()
dict_df['station_name'] = dict_df['station_name'].str.strip()

# Create a dictionary of station names and ids
enterprise_dict = dict(zip(dict_df['station_name'], dict_df['station_id']))

# Replace station_name in org_df with corresponding station_id
org_df['station_name'] = org_df['station_name'].map(enterprise_dict).fillna(org_df['station_name'])

# Save the updated DataFrame to a new Excel file
updated_org_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/气瓶2/updated-station-id-replaced1025.xlsx'  # Replace with your file path
org_df.to_excel(updated_org_file_path, index=False)

print(f"Updated Excel file with correct org_id column created: {updated_org_file_path}")
