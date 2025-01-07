import os
import pdfplumber
import pandas as pd

# Define the root folder containing the project with subfolders
root_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2024\05\Other"  # Replace with your root folder path

# Output Excel file
output_excel = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2024\05\New_Ratings_May_2024.xlsx"

# List to store extracted data from all PDFs
all_data = []

# Loop through the root folder and all subfolders to find PDFs
for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".pdf"):  # Only process PDF files
            pdf_file = os.path.join(root, file)
            print(f"Processing {pdf_file}...")  # For debugging, print the current file being processed
            
            # Initialize variables for extracted data
            quick_values, pipe_rating_values, rating_index_values = [], [], []
            
            # Open the PDF and extract the ratings information
            with pdfplumber.open(pdf_file) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        # Search for the ratings section
                        lines = text.split("\n")
                        for i, line in enumerate(lines):
                            if "Quick:" in line:
                                # Extract Quick values from the current line
                                quick_values = line.replace("Quick:", "").strip().split()
                            if "Pipe Rating:" in line:
                                # Extract Pipe Rating values from two lines below "Quick:"
                                pipe_rating_values = line.replace("Pipe Rating:", "").strip().split()
                            if "Rating Index:" in line:
                                # Extract Rating Index values from four lines below "Quick:"
                                rating_index_values = line.replace("Rating Index:", "").strip().split()
                                
                                break  # Exit once ratings are found

            # Ensure there are exactly 3 values in each list
            if len(quick_values) == 3 and len(pipe_rating_values) == 3 and len(rating_index_values) == 3:
                # Prepare data for the Excel file
                data = [
                    [
                        file,  # File Name
                        quick_values[0], pipe_rating_values[0], rating_index_values[0],
                        quick_values[1], pipe_rating_values[1], rating_index_values[1],
                        quick_values[2], pipe_rating_values[2], rating_index_values[2]
                    ]
                ]
                all_data.extend(data)  # Add the extracted data to the list of all data
            else:
                print(f"Error: {pdf_file} does not contain exactly 3 values for Quick, Pipe Rating, and Rating Index.")

# Create column headers
columns = [
    "File Name", "Quick 1", "Pipe Rating 1", "Rating Index 1",
    "Quick 2", "Pipe Rating 2", "Rating Index 2",
    "Quick 3", "Pipe Rating 3", "Rating Index 3"
]

# Create a DataFrame with all extracted data
df = pd.DataFrame(all_data, columns=columns)

# Save all the extracted data to the Excel file
df.to_excel(output_excel, index=False, startrow=2)  # Write to row 3 (0-based index + 2)

print(f"All ratings data has been successfully extracted and saved to {output_excel}")
