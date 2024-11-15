import os
import shutil

# Set the paths to your folders
pdf_folder_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\07 pdf\New folder'
project_folder_path = r'X:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Other\2023\07'

# Loop through each PDF file in the pdf folder
for pdf_file in os.listdir(pdf_folder_path):
    if pdf_file.endswith('.pdf'):
        # Step 1: Remove the space between the second and third underscore
        parts = pdf_file.split('_')
        if len(parts) > 2:
            parts[2] = parts[2].replace(' ', '')  # Remove the space
            new_pdf_file = '_'.join(parts)  # Rejoin parts into a new file name
        else:
            new_pdf_file = pdf_file  # If format doesn't match, keep original name

        # Step 2: Remove the last 7 characters before the extension
        name, extension = os.path.splitext(new_pdf_file)
        modified_pdf_file = name[:-7] + extension
        
        # Rename the PDF file to reflect both modifications
        old_path = os.path.join(pdf_folder_path, pdf_file)
        new_path = os.path.join(pdf_folder_path, modified_pdf_file)
        os.rename(old_path, new_path)

        # Extract prefix and suffix for folder matching
        pdf_name_parts = modified_pdf_file.split('_')
        prefix = pdf_name_parts[0]
        suffix = pdf_name_parts[-1].split('.')[0]  # Remove the .pdf extension from the suffix
        
        # Step 3: Move the file to the correct project folder
        for project_folder in os.listdir(project_folder_path):
            # Check if the folder matches the extracted prefix and suffix from the PDF
            if project_folder.startswith(prefix) and project_folder.endswith(suffix):
                # Define the destination path
                destination_path = os.path.join(project_folder_path, project_folder, modified_pdf_file)
                
                # Move the PDF file to the matched project folder
                shutil.move(new_path, destination_path)
                print(f'Moved {modified_pdf_file} to {project_folder}')
                break  # Stop searching once the PDF is moved

print("PDF renaming and moving complete.")
