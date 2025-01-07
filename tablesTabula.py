import pdfplumber
import pandas as pd  # Make sure pandas is imported

# Specify the input PDF file and output Excel file
pdf_file = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\GP001106-073911_20230128_0810_Upstream.pdf"
output_excel = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\Ratings.xlsx"

with pdfplumber.open(pdf_file) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"Page {page_number} Text:\n")
        print(page.extract_text())
        print("-" * 50)
