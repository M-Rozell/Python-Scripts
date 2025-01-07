import os
import pdfplumber
import pandas as pd
import re

# Define the root folder containing the project with subfolders
root_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\09\Other"
output_excel = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2023\09\Ratings.xlsx"

# Ensure the directory for the output file exists
os.makedirs(os.path.dirname(output_excel), exist_ok=True)

# List to store extracted data from all PDFs
all_data = []
max_values = 0  # Track the maximum number of values

# Regex pattern to match lines starting with "GP" and ending with "V", allowing spaces before "V"
pattern = r"^GP\d{6}-\d{6}_"

# Tracking processed files
total_files = 0
processed_files = 0

# Loop through the root folder and all subfolders to find PDFs
for root, dirs, files in os.walk(root_folder):
    for file in files:
        total_files += 1
        if file.endswith(".pdf"):
            processed_files += 1
            pdf_file = os.path.join(root, file)
            print(f"Processing {pdf_file}...")
            
            # Initialize variable to store the extracted line
            extracted_line = ""
            try:
                with pdfplumber.open(pdf_file) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            # Split the text into lines
                            lines = text.split("\n")
                            for line in lines:
                                if re.match(pattern, line):
                                    extracted_line = line
                                    break

                # Split and adjust values if "GP" line found
                if extracted_line:
                    values = extracted_line.split()
                    adjusted_values = []
                    for value in values:
                        adjusted_values.append(value)
                        if value == "0000":
                            adjusted_values.append("0")
                    max_values = max(max_values, len(adjusted_values))
                    all_data.append([file] + adjusted_values)
                else:
                    print(f"Warning: No 'GP' line ending with 'V' found in {file}")
                    all_data.append([file] + [""] * 20)

            except Exception as e:
                print(f"Error processing {file}: {e}")

# Exit if no 'GP' lines found
if max_values == 0:
    print("No 'GP' lines ending with 'V' found in any PDF. Exiting.")
    exit()

# Create column headers
columns = ["File Name"] + [f"Value {i+1}" for i in range(max_values)]

# Create a DataFrame with all extracted lines
df = pd.DataFrame(all_data, columns=columns)

# Save all the extracted data to the Excel file
df.to_excel(output_excel, index=False, startrow=2)

print(f"Total files scanned: {total_files}")
print(f"PDF files processed: {processed_files}")
print(f"All extracted lines have been successfully saved to {output_excel}")
