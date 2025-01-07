from PyPDF2 import PdfReader

def check_if_pdf_has_tables(pdf_file):
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text = page.extract_text()
        if "\t" in text or ("|") in text or any(line.count(" ") > 5 for line in text.split("\n")):
            # Check for tabular delimiters or frequent spaces
            return True
    return False

# Example usage
pdf_path = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\GP009040-089719_20240611_1202_Downstream.pdf"
if check_if_pdf_has_tables(pdf_path):
    print("The PDF likely contains tables.")
else:
    print("No tables detected in the PDF.")
