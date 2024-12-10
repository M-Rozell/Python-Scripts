import pdfplumber
import pandas as pd
import os

# Function to extract tables and save them to a specified folder
def extract_tables_to_excel(pdf_path, output_folder, output_filename="extracted_tables.xlsx"):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Full path for the Excel file
    output_path = os.path.join(output_folder, output_filename)
    
    with pdfplumber.open(pdf_path) as pdf:
        with pd.ExcelWriter(output_path) as writer:
            for page_number, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables()
                for table_index, table in enumerate(tables, start=1):
                    # Convert table to a DataFrame
                    df = pd.DataFrame(table)
                    
                    # Name the sheet based on the page and table index
                    sheet_name = f"Page{page_number}_Table{table_index}"
                    
                    # Save the DataFrame to the Excel file
                    df.to_excel(writer, index=False, header=False, sheet_name=sheet_name)
                    print(f"Saved Table {table_index} from Page {page_number} in '{output_path}'")
    
    print(f"All tables saved to: {output_path}")

# Input PDF path
pdf_path = r"C:\Users\MaggieRozell\Desktop\Trash\Actual Trash\GP002012-017247_20220526_1525_Downstream.pdf"

# Specify the output folder and file name
output_folder = r"C:\Users\MaggieRozell\Desktop\Trash\Actual Trash"  # Change to your desired folder
output_filename = r"C:\Users\MaggieRozell\Desktop\Trash\Actual Trash\Practice.xlsx"

# Run the function
extract_tables_to_excel(pdf_path, output_folder, output_filename)



