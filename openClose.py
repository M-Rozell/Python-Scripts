import os
import subprocess

# Set the path to your project folder
project_folder = r"C:\Users\MaggieRozell\Desktop\Trash\Actual Trash\open_close\Practice file"

# Loop through each subfolder and process .ptdx files
for root, dirs, files in os.walk(project_folder):
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(root, file)
            print(f"Processing file: {file_path}")
            
            # Open the file using the associated application (modify as needed)
            try:
                # Change the command to the appropriate one for PipeTech if necessary
                process = subprocess.Popen(['start', file_path], shell=True)
                process.wait()  # Wait for the process to finish
                print(f"Successfully opened and closed: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
