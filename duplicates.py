import os
import shutil

# Define the path to the main project folder and the Duplicates folder
project_folder = r'Z:\017560-17 - JEFFCO 2024 AMP06 SDIR\AMP06_2024_Project\December 2024\Other'
duplicates_folder = r'Z:\017560-17 - JEFFCO 2024 AMP06 SDIR\AMP06_2024_Project\December 2024'
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