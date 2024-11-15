import os
import shutil

# Define the path to the main project folder and the Duplicates folder
project_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\05'
duplicates_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\05\Duplicates'
# Create the Duplicates folder if it doesn't exist
os.makedirs(duplicates_folder, exist_ok=True)

# Loop through each folder in the project directory
for folder_name in os.listdir(project_folder):
    folder_path = os.path.join(project_folder, folder_name)
    
    # Check if it's a directory (folder)
    if os.path.isdir(folder_path):
        # Get a list of PDF files in the folder
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
        
        # If there are exactly 2 PDFs, move the folder to Duplicates
        if len(pdf_files) == 2:
            # Move the folder to the Duplicates folder
            shutil.move(folder_path, os.path.join(duplicates_folder, folder_name))
            print(f"Moved '{folder_name}' to Duplicates")