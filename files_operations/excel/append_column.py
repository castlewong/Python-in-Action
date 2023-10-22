import pandas as pd


def add_text_to_column_by_name(excel_path, column_name, text_to_add, output_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(excel_path)

    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Append text to each cell in the specified column
        df[column_name] = df[column_name].astype(str) + text_to_add

        # Save the modified DataFrame back to a new Excel file
        df.to_excel(output_path, index=False)
        print(f"Text added to column '{column_name}' and file saved as {output_path}")
    else:
        print(f"Column '{column_name}' not found in the Excel file.")


# Example usage
excel_file_path = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/updated-merged_output_flask-after-join.xlsx'  # Replace with your actual Excel file
output_excel_file = '/Users/wilburwong/Nutstore Files/A_Company/A盐城液化气/updated-merged_output_flask-after-join-appedTEXT.xlsx'  # Replace with the desired output file path
column_name = 'station_id'  # The column you want to modify
text = '场站'  # The text you want to append to each cell in the column

add_text_to_column_by_name(excel_file_path, column_name, text, output_excel_file)
