import pandas as pd
# 从另一个xlsx获取sheet名
# Load the Excel file into a DataFrame
df = pd.read_excel('type_fromDB.xlsx')

# print(df['type_name'].unique())

# Group the data by type_name and iterate over each group
for name, group_df in df.groupby('type_name'):

    # Create a new Excel file with a sheet for this group
    writer = pd.ExcelWriter(f'{name}.xlsx', engine='xlsxwriter')

    # Write the group's data to the new sheet
    group_df.to_excel(writer, sheet_name=name, index=False)

    # Save the new Excel file
    writer.save()


def group_data_to_excel(df, group_col):
    """
    Groups a pandas DataFrame by a specified column and exports each group's data to a separate Excel file.

    Args:
        df (pandas.DataFrame): The DataFrame to group and export.
        group_col (str): The name of the column to group the DataFrame by.

    Returns:
        None
    """

    # Group the data by the specified column
    grouped_data = df.groupby(group_col)

    # Iterate over each group and write its data to a new Excel file
    for group_name, group_df in grouped_data:
        # Create a new Excel file with a sheet for this group
        writer = pd.ExcelWriter(f'{group_name}.xlsx', engine='xlsxwriter')

        # Write the group's data to the new sheet
        group_df.to_excel(writer, sheet_name=group_name, index=False)

        # Save the new Excel file
        writer.save()


