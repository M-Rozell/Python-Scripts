import pdfplumber
import pandas as pd
import os

# Define a function to extract data from a single PDF
def extract_data_from_pdf(pdf_path):
    all_rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()  # Extract all tables on the page
            if tables:
                for table in tables:
                    # Append all rows except the header row
                    all_rows.extend(table[1:])  # Skip the first row (header)
    return all_rows

# Specify the column headers (only once)
column_headers = ["Segment", "Size", "Material","Length","Basin","Services","Location","Depth"]  # Replace with actual column names


# Process multiple PDFs
pdf_files = [r"C:\Users\MaggieRozell\Desktop\Trash\missing videos\FY25 PB Segment Maps .pdf"]  # Add paths to your PDF files


for pdf_path in pdf_files:
    # Extract data from the current PDF
    extracted_data = extract_data_from_pdf(pdf_path)

     # Create a DataFrame with consistent headers
    df = pd.DataFrame(extracted_data, columns=column_headers)

    # Determine the output Excel file path
    pdf_dir = os.path.dirname(pdf_path)  # Get the directory of the PDF
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]  # Get the PDF name without extension
    excel_path = os.path.join(pdf_dir, f"{pdf_name}.xlsx")  # Set the Excel file name

    # Save the DataFrame to Excel
    df.to_excel(excel_path, index=False)
    print(f"Data from '{pdf_path}' saved to '{excel_path}'.")
