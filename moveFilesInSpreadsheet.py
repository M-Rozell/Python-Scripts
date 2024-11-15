import os
import shutil
import pandas as pd

# Paths (update these paths with your actual folder locations)
excel_file_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\Sept 23\TwentyNewList.xlsx'
project_folder_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\09'
destination_folder_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\Sept 23\TwentyNew'

# Load the Excel file into a DataFrame
df = pd.read_excel(excel_file_path, sheet_name='Sheet1', header=0)

# Print the column names to check their labels
print("Column Name:", df.columns)

# Convert a column to a list (replace 'ColumnName' with the name of your column)
#column_list = df['FolderName'].tolist()
#print("Column as a list:", column_list)

# Load the list of folder names from the Excel file
folder_list_df = pd.read_excel(excel_file_path)  # Reads Excel with "FolderName" as column header in row 1
folder_names = folder_list_df['FolderName'].tolist()  # Column "FolderName" values as a list

# Counter for the moved folders
moved_count = 0

# Loop through each folder in the project folder
for folder_name in os.listdir(project_folder_path):
    folder_path = os.path.join(project_folder_path, folder_name)
    
    # Remove characters after the last underscore
    base_folder_name = folder_name.rpartition('_')[0] if '_' in folder_name else folder_name
    
    # Check if it's a folder and if the modified name is in the list
    if os.path.isdir(folder_path) and base_folder_name in folder_names:
        # Move the folder to the destination
        shutil.move(folder_path, os.path.join(destination_folder_path, folder_name))
        moved_count += 1
        print(f"Moved: {folder_name}")

print(f"Folder move complete. Total folders moved: {moved_count}")








