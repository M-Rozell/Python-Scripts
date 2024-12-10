from tabula import read_pdf
from openpyxl import Workbook

def extract_first_page_to_excel_tabula(pdf_file, excel_file):
    try:
        # Step 1: Extract tables from the first page
        tables = read_pdf(pdf_file, pages="1", multiple_tables=True, lattice=True)

        if not tables:
            print("No tables found on the first page.")
            return

        # Step 2: Write the extracted tables into an Excel file
        wb = Workbook()
        ws = wb.active
        ws.title = "Extracted Data"

        # Add each table to the spreadsheet
        row_offset = 1
        for table in tables:
            for row in table.values:
                for col_idx, cell in enumerate(row, start=1):
                    ws.cell(row=row_offset, column=col_idx, value=cell)
                row_offset += 1
            row_offset += 1  # Add a blank row between tables

        # Save the Excel file
        wb.save(excel_file)
        print(f"Data from the first page has been written to {excel_file}")
    except Exception as e:
        print(f"Error: {e}")

# Usage
pdf_path = r"C:\Users\MaggieRozell\Desktop\Trash\Actual Trash\GP002012-017247_20220526_1525_Downstream.pdf"  # Replace with the path to your PDF file
excel_path = r"C:\Users\MaggieRozell\Desktop\x\test.xlxs"  # Replace with the desired Excel file path

extract_first_page_to_excel_tabula(pdf_path, excel_path)



