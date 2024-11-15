import os
import shutil

# Set the paths to your folders
project_folder_with_mp4s = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\JEFFCO - JUNE 2023'
project_folder_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\NoMP4\2023\06'

# Counter to keep track of how many files were copied
copied_files_count = 0

# Loop through each MP4 file in the mp4 folder where MP4s are in one folder
#for mp4_file in os.listdir(mp4_folder_path):
    #if mp4_file.endswith('.mp4'):


# Recursively walk through all subdirectories in the main project folder
for root, dirs, files in os.walk(project_folder_with_mp4s):
    for file in files:
        # Only process the file if it has an exact .mp4 extension
        if not file.lower().endswith('.mp4'):
            continue  # Skip any file that is not an MP4

        # Step 1: Attempt to split the filename by underscores and remove space in specific part
        parts = file.split('_')
        
        # Only proceed if there are at least three parts after splitting
        if len(parts) > 2:
            # Remove any space in the third part of the filename
            parts[2] = parts[2].replace(' ', '')
            new_mp4_file = '_'.join(parts)  # Rejoin parts into a modified name
        else:
            # If the filename doesn't match the expected format, skip modification
            new_mp4_file = file 

        # Step 2: Remove the last 7 characters before the extension
        name, extension = os.path.splitext(new_mp4_file)
        modified_mp4_file = name[:-7] + extension
        
        # Rename the MP4 file to reflect both modifications (without renaming the actual file in the folder)
        original_path = os.path.join(root, file)
        
        # Extract prefix and suffix for folder matching
        mp4_name_parts = modified_mp4_file.split('_')
        prefix = mp4_name_parts[0]
        suffix = mp4_name_parts[-1].split('.')[0]  # Remove the .mp4 extension from the suffix
        
        # Step 3: Copy the file to the correct project folder
        for project_folder in os.listdir(project_folder_path):
            # Check if the folder matches the extracted prefix and suffix from the MP4
            if project_folder.startswith(prefix) and project_folder.endswith(suffix):
                # Define the destination path
                destination_path = os.path.join(project_folder_path, project_folder, modified_mp4_file)
                
                # Copy the MP4 file to the matched project folder
                shutil.copy2(original_path, destination_path)
                print(f'Copied {file} as {modified_mp4_file} to {project_folder}')
                
                # Increment the copied files count
                copied_files_count += 1
                break  # Stop searching once the MP4 is copied

# Print the total number of files that were copied
print(f"Total MP4 files copied: {copied_files_count}")
