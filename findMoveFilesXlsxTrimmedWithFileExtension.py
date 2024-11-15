import os
import shutil
import pandas as pd

# Define paths
excel_file_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\02\folder_list.xlsx'  # Path to the Excel file with folder names
source_root_folder = r'V:\017560-12 - JEFFCO 2022 AMP08\JEFFCO\FEBRUARY\JEFFCO - FEBRUARY 2023'  # Path to the main project folder with subfolders
destination_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\02\Missing files'  # Path where folders should be copied

# Load file names from Excel, skipping the header row
file_names_df = pd.read_excel(excel_file_path)
file_names = file_names_df.iloc[:, 0].tolist()  # Assuming file names are in the first column

# Trim file names to the first 27 characters
file_names_trimmed = [name[:27] for name in file_names]

# Check each file in the source root folder
for root, dirs, files in os.walk(source_root_folder):
    for file in files:
        # Check if the file is an mp4 and if its name (first 27 chars) matches any in the list
        if file.endswith(".mp4") and file[:27] in file_names_trimmed:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)

            # Copy file to destination
            if not os.path.exists(destination_path):
                shutil.copy2(source_path, destination_path)  # copy2 preserves metadata
                print(f"Copied '{file}' to '{destination_path}'")
            else:
                print(f"File '{file}' already exists in the destination.")
