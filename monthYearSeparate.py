import os
import shutil
import re

# Define the path to the 'Other' folder
other_folder_path = 'X:\\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\\Other'

# Regular expression to match dates in the YYYYMMDD format
date_pattern = re.compile(r'(\d{4})(\d{2})(\d{2})')

# Process each folder in the 'Other' directory
for folder_name in os.listdir(other_folder_path):
    folder_path = os.path.join(other_folder_path, folder_name)

    # Check if the item is a folder
    if os.path.isdir(folder_path):
        # Match the YYYYMMDD pattern in the folder name
        match = date_pattern.search(folder_name)
        
        if match:
            # Extract year and month from the matched date
            year = match.group(1)
            month = match.group(2)
            
            # Define the destination path based on year and month
            destination_folder = os.path.join(other_folder_path, year, month)
            
            # Create year/month folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)
            
            # Move the folder to the destination
            shutil.move(folder_path, os.path.join(destination_folder, folder_name))
            print(f"Moved {folder_name} to {destination_folder}")

print("Folders have been organized by month and year.")
