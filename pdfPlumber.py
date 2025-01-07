import pdfplumber
import pandas as pd
import os

# Create an output directory
os.makedirs("extracted_tables", exist_ok=True)

# Open the PDF
pdf_path = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\GP009015-080666_20230728_1205_U_D_Post.pdf"
with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        # Extract tables from the page
        tables = page.extract_tables()
        
        # Save each table as a separate Excel file
        for table_index, table in enumerate(tables, start=1):
            # Convert table to a DataFrame
            df = pd.DataFrame(table)
            
output_path = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\Ratings.xlsx"
with pd.ExcelWriter(output_path) as writer:
    for page_number, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        for table_index, table in enumerate(tables, start=1):
            df = pd.DataFrame(table)
            sheet_name = f"Page{page_number}_Table{table_index}"
            df.to_excel(writer, index=False, header=False, sheet_name=sheet_name)
print(f"All tables saved to {output_path}")




