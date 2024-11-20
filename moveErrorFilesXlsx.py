import os
import shutil
import pandas as pd

# Define the path to the Excel file and the root project folder
excel_file = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2022\07\errorLog.xlsx'
project_root = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2022\07\Other'

# Load the Excel file into a DataFrame
df = pd.read_excel(excel_file, header=0)

# Print the column names to check their labels (for troubleshooting)
print("Column names:", df.columns)

# Update these variables to match the exact column names in your Excel file
column_b = 'SourceFilePath'   # Replace 'B' with the actual name of the second column if different
column_f = 'ProblemType'   # Replace 'F' with the actual name of the sixth column if different

# Iterate through each row, starting from row 2 (pandas handles headers automatically)
for index, row in df.iterrows():
    try:
        # Get the full path from column B and the target folder name from column F
        full_path = row[column_b]
        target_folder_name = row[column_f]
        
        # Extract the folder name without the file extension
        folder_name_with_ext = os.path.basename(full_path)
        folder_name, _ = os.path.splitext(folder_name_with_ext)  # Exclude the file extension
        
        # Define the source folder path and the target path
        source_folder_path = os.path.join(project_root, folder_name)
        target_folder_path = os.path.join(project_root, target_folder_name)
        
        # Make the target directory if it doesn't exist
        os.makedirs(target_folder_path, exist_ok=True)
        
        # Move the folder to the target directory
        if os.path.isdir(source_folder_path):
            shutil.move(source_folder_path, target_folder_path)
            print(f"Moved '{folder_name}' to '{target_folder_path}'")
        else:
            print(f"Folder '{folder_name}' not found in the project directory")
    except KeyError as e:
        print(f"Column error: {e}")
        break



