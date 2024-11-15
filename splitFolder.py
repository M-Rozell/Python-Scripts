import os
import shutil

# Set the path to your project folder
project_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\03'
# Create a destination folder for folders without MP4 files
destination_folder = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\mp4'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through each folder in the project folder
for foldername in os.listdir(project_folder):
    folder_path = os.path.join(project_folder, foldername)
    if os.path.isdir(folder_path):
        # Check for MP4 files in the current folder
        has_mp4 = any(file.endswith('.mp4') for file in os.listdir(folder_path))
        # If there are no MP4 files, move the folder to the destination
        if not has_mp4:
            shutil.move(folder_path, os.path.join(destination_folder, foldername))

print("Folders without MP4 files have been moved.")
