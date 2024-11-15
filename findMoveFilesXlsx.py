import os
import shutil
import pandas as pd

# Define paths
excel_file_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\02\folder_list.xlsx'  # Path to the Excel file with folder names
source_root_folder = r'V:\017560-12 - JEFFCO 2022 AMP08\JEFFCO\FEBRUARY\JEFFCO - FEBRUARY 2023'  # Path to the main project folder with subfolders
destination_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\02\Missing files'  # Path where folders should be copied

# Load folder names from Excel
folder_names_df = pd.read_excel(excel_file_path)
folder_names = folder_names_df.iloc[:, 0].tolist()  # Assuming folder names are in the first column and there is a header

# If there is no header
#folder_names_df = pd.read_excel(excel_file_path, header=None)
folder_names = folder_names_df[0].tolist()

# Check each folder in the source root folder
for root, dirs, files in os.walk(source_root_folder):
    for folder in dirs:
        if folder in folder_names:
            source_path = os.path.join(root, folder)
            destination_path = os.path.join(destination_folder, folder)

            # Copy folder to destination
            if not os.path.exists(destination_path):
                shutil.copytree(source_path, destination_path)
                print(f"Copied '{folder}' to '{destination_path}'")
            else:
                print(f"Folder '{folder}' already exists in the destination.")
