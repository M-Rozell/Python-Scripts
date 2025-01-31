import os
import pandas as pd

# Set your project folder path
project_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\Project\Other"

# List to store folder paths and PDF counts
data = []
folder_count = 0  # Counter for folders with 2+ PDFs

# Loop through all subfolders
for root, dirs, files in os.walk(project_folder):
    pdf_count = sum(1 for file in files if file.lower().endswith('.pdf'))
    
    if pdf_count >= 2:
        data.append([root, pdf_count])
        folder_count += 1  # Increment count

# Convert to a DataFrame
df = pd.DataFrame(data, columns=["Folder Path", "PDF Count"])

# Save to an Excel file
output_file = os.path.join(project_folder, "pdf_folders.xlsx")
df.to_excel(output_file, index=False, engine="openpyxl")

# Print results in console
print(f"Total folders with 2 or more PDFs: {folder_count}")
print(f"Excel file saved at: {output_file}")
