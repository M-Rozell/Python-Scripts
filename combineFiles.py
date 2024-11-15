import os
import shutil

# Paths to the source folder (with PDFs) and target folder
source_folder = r"X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\07 pdf"
destination_folder= r"X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\07"

# Counter for the moved folders
moved_count = 0

# Iterate through all PDFs in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.pdf'):
        pdf_name = os.path.splitext(filename)[0]  # Get the filename without extension
        pdf_path = os.path.join(source_folder, filename)
        target_folder = os.path.join(destination_folder, pdf_name)

        # Check if a folder with the same name exists
        if os.path.isdir(target_folder):
            shutil.move(pdf_path, os.path.join(target_folder, filename))
            moved_count += 1
            print(f"Moved '{filename}' to '{target_folder}'")
        else:
            print(f"Folder '{target_folder}' does not exist. Skipping '{filename}'.")

print(f"Task complete. {moved_count} files moved")
