import os
import shutil

# Define the source and destination paths
source_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\Inspections"
destination_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\Split"

# Number of groups to split into
num_groups = 10

def split_folders(source, destination, groups):
    # Get all folder names in the source directory
    subfolders = [f for f in os.listdir(source) if os.path.isdir(os.path.join(source, f))]
    total_subfolders = len(subfolders)

    # Check if the split is possible
    if total_subfolders != groups * (total_subfolders // groups):
        print("Warning: The folder count isn't evenly divisible by the groups. Extra folders will remain.")
    
    # Calculate number of folders per group
    folders_per_group = total_subfolders // groups

    # Create target groups and move folders
    for i in range(groups):
        group_path = os.path.join(destination, f"group_{i+1}")
        os.makedirs(group_path, exist_ok=True)
        
        start_index = i * folders_per_group
        end_index = start_index + folders_per_group
        group_folders = subfolders[start_index:end_index]

        for folder in group_folders:
            src = os.path.join(source, folder)
            dst = os.path.join(group_path, folder)
            shutil.move(src, dst)

    print(f"Folders have been split into {groups} groups and moved to {destination}")

# Execute the function
split_folders(source_folder, destination_folder, num_groups)
