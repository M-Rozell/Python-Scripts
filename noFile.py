import os
import shutil

# Define the path to the main project folder and the custom "NoMP4" folder
project_folder = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\10\Inspections'
no_mp4_folder = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\10\New folder'

# Create the "NoMP4" folder if it doesn't exist
os.makedirs(no_mp4_folder, exist_ok=True)

# Loop through each folder in the project directory
for folder_name in os.listdir(project_folder):
    folder_path = os.path.join(project_folder, folder_name)
    
    # Check if it's a directory (folder)
    if os.path.isdir(folder_path):
        # Get a list of MP4 files in the folder
        mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
        
        # If there are no MP4 files, move the folder to the "NoFile" folder
        if len(mp4_files) == 0:
            # Move the folder to the "NoMP4" folder
            shutil.move(folder_path, os.path.join(no_mp4_folder, folder_name))
            print(f"Moved '{folder_name}' to NoFile")
