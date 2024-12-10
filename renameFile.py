import os

# Replace this with the folder containing your PDF files
folder_path = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\09\pdf"  # Use the appropriate path on your system

count = 0

# Check if the folder exists
if not os.path.isdir(folder_path):
    print(f"The folder {folder_path} does not exist. Please check the path.")
else:
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file ends with "_D_D_Post.pdf"
        if file_name.endswith("_D_Post.pdf"):
            # Create the new file name
            new_name = file_name.replace("_D_Post.pdf", "_Downstream.pdf")
            # Build full paths
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            # Rename the file
            os.rename(old_path, new_path)
            count += 1
            print(f"Renamed: {file_name} -> {new_name}")

    print(f"Renaming {count} complete!")
