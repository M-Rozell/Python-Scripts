import os
import pdfplumber
import pandas as pd
import re  # Import regular expression module

# Define the root folder containing the project with subfolders
root_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\08\Other"  # Replace with your root folder path

# Output Excel file
output_excel = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\08\Old_Ratings_August__2023.xlsx"

# List to store extracted data from all PDFs
all_data = []

# Track the maximum number of values in any line to set the correct number of columns
max_values = 0

# Simplified regex pattern to match lines starting with "GP"
pattern = r"^GP"

# Loop through the root folder and all subfolders to find PDFs
for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".pdf"):  # Only process PDF files
            pdf_file = os.path.join(root, file)
            print(f"Processing {pdf_file}...")  # For debugging, print the current file being processed
            
            # Initialize variable to store the extracted line
            extracted_line = ""

            # Open the PDF and extract the text
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        # Split the text into lines
                        lines = text.split("\n")
                        for line in lines:
                            # Check if the line starts with "GP"
                            if re.match(pattern, line):
                                extracted_line = line
                                break  # Exit once the line is found

            # Split the extracted line by spaces and store as separate values
            if extracted_line:
                values = extracted_line.split()  # Split by spaces

                # Adjust values if "0000" is encountered (insert 0 in the next column)
                adjusted_values = []
                for i, value in enumerate(values):
                    adjusted_values.append(value)
                    if value == "0000":
                        adjusted_values.append("0")  # Insert 0 in the next column

                max_values = max(max_values, len(adjusted_values))  # Track the max number of columns
                # Add the file name followed by the adjusted values
                all_data.append([file] + adjusted_values)
            else:
                # If no line found, add an empty row
                all_data.append([file] + [""] * 20)  # Adjust 20 to the max number of columns expected

# Create column headers
columns = ["File Name"] + [f"Value {i+1}" for i in range(max_values)]

# Create a DataFrame with all extracted lines
df = pd.DataFrame(all_data, columns=columns)

# Save all the extracted data to the Excel file
df.to_excel(output_excel, index=False, startrow=2)  # Write to row 3 (0-based index + 2)

print(f"All extracted lines have been successfully saved to {output_excel}")