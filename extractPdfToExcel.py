from PyPDF2 import PdfReader
from openpyxl import Workbook

# Function to extract the segment from the PDF
def extract_segment_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text = page.extract_text()
        if "Segment" in text:
            # Adjust extraction logic based on how "Segment" appears
            lines = text.split("\n")
            for line in lines:
                if "Segment" in line:
                    # Extract the relevant part after "Segment"
                    segment = line.split("Segment")[-1].strip()
                    return segment
    return None

# Write the extracted segment to an Excel file
def write_segment_to_excel(segment, excel_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    # Place "Segment" value in the first column, third row
    ws.cell(row=3, column=1, value=segment)

    wb.save(excel_file)
    print(f"Segment saved to {excel_file} in first column, third row.")

# Main logic
pdf_path = r"C:\Users\MaggieRozell\Desktop\Trash\Actual TrashGP002012-017247_20220526_1525_Downstream\GP002012-017247_20220526_1525_Downstream.pdf"  # Replace with your PDF file path
excel_path = r"C:\Users\MaggieRozell\Desktop\x\PDFconversion.xlsx"  # Replace with desired Excel output path

# Extract and write
segment = extract_segment_from_pdf(pdf_path)
if segment:
    write_segment_to_excel(segment, excel_path)
else:
    print("Segment not found in the PDF.")
