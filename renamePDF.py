import os

# Set your folder path here
folder_path = 'X:\\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\\Other\\2022\\May 2022 PDF'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Split the file name and extension
        name, extension = os.path.splitext(filename)
        
        # Rename by removing the last 7 characters of the name
        new_name = name[:-7] + extension
        
        # Get the full path for the old and new file names
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)

print("Renaming complete.")