import os
import shutil
import pandas as pd

# Define paths
excel_file_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\02\folder_list.xlsx'  # Path to the Excel file with folder names
source_root_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\09'  # Path to the main project folder with subfolders
destination_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\02\Missing files'  # Path where folders should be copied

# Load folder names from Excel, skipping the header row
folder_names_df = pd.read_excel(excel_file_path)
folder_names = folder_names_df.iloc[:, 0].tolist()  # Assuming folder names are in the first column

# Trim folder names to the first 27 characters
folder_names_trimmed = [name[:27] for name in folder_names]

# Check each folder in the source root folder
for root, dirs, files in os.walk(source_root_folder):
    for folder in dirs:
        if folder[:27] in folder_names_trimmed:
            source_path = os.path.join(root, folder)
            destination_path = os.path.join(destination_folder, folder)

            # Copy folder to destination
            if not os.path.exists(destination_path):
                shutil.copytree(source_path, destination_path)
                print(f"Copied '{folder}' to '{destination_path}'")
            else:
                print(f"Folder '{folder}' already exists in the destination.")
