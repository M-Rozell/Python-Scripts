import os
import shutil

# Set the paths to your project folders
pdf_folder_path = 'X:\\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\\Other\\2022\\May 2022 PDF'
project_folder_path = 'X:\\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\\Other\\2022\\05'

# Loop through each PDF file in the pdf folder
for pdf_file in os.listdir(pdf_folder_path):
    if pdf_file.endswith('.pdf'):
        # Extract the parts of the PDF name before the first underscore and after the last underscore
        pdf_name_parts = pdf_file.split('_')
        prefix = pdf_name_parts[0]
        suffix = pdf_name_parts[-1].split('.')[0]  # Remove the .pdf extension from the suffix
        
 # Loop through each folder in the project folder
        for project_folder in os.listdir(project_folder_path):
            # Check if the folder matches the extracted prefix and suffix from the PDF
            if project_folder.startswith(prefix) and project_folder.endswith(suffix):
                # Define source and destination paths
                source_path = os.path.join(pdf_folder_path, pdf_file)
                destination_path = os.path.join(project_folder_path, project_folder, pdf_file)
                
                # Move the PDF file to the matched project folder
                shutil.move(source_path, destination_path)
                print(f'Moved {pdf_file} to {project_folder}')
                break  # Stop searching for this PDF once it's moved

print("All PDFs have been moved to their respective folders.")