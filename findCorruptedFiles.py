import os
import cv2
import shutil

def is_mp4_file_corrupted(filepath):
    try:
        cap = cv2.VideoCapture(filepath)
        if not cap.isOpened():
            return True
        ret, _ = cap.read()
        cap.release()
        return not ret
    except Exception as e:
        print(f"Error opening file {filepath}: {e}")
        return True

def find_and_move_corrupted_folders(root_folder, target_folder):
    corrupted_folders = set()
    
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)
    
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith('.mp4'):
                filepath = os.path.join(dirpath, filename)
                if is_mp4_file_corrupted(filepath):
                    corrupted_folders.add(dirpath)
                    break  # No need to check further files in this folder
    
    # Move the corrupted folders to the target location
    for folder in corrupted_folders:
        # Counter for the moved folders
        moved_count = 0
        folder_name = os.path.basename(folder)
        destination = os.path.join(target_folder, folder_name)
        print(f"Moving folder: {folder} -> {destination}")
        shutil.move(folder, destination)
        moved_count += 1
        print(f"Folder move complete. Total folders moved: {moved_count}")

# Specify your root folder path and target folder path
root_folder = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2022\07\Other'
target_folder = r'Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2022\07\Duplicates'
find_and_move_corrupted_folders(root_folder, target_folder)
