import os
import xml.etree.ElementTree as ET
from openpyxl import Workbook

def extract_to_excel(folder_path, excel_file_path):
    # Ensure the provided folder path exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return
    
    # Create a new workbook and add a sheet
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Extracted Data"
    # Add headers to the Excel file
    sheet.append(["File Name", "Upstream_AP", "Downstream_AP", "Pipe_Segment_Reference"])

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ptdX"):  # Look for .ptdx files
                ptdx_file_path = os.path.join(root, file)
                try:
                    # Parse the .ptdx file as XML
                    print(f"Processing: {ptdx_file_path}")
                    tree = ET.parse(ptdx_file_path)  # Validate XML structure
                    root_element = tree.getroot()

                    # Extract the values from <A_002>
                    a_002 = root_element.find(".//A_002")
                    if a_002 is not None:
                        upstream_ap = a_002.find("Upstream_AP").text if a_002.find("Upstream_AP") is not None else ""
                        downstream_ap = a_002.find("Downstream_AP").text if a_002.find("Downstream_AP") is not None else ""
                        pipe_segment_ref = a_002.find("Pipe_Segment_Reference").text if a_002.find("Pipe_Segment_Reference") is not None else ""

                        # Append the extracted data to the Excel file
                        sheet.append([file, upstream_ap, downstream_ap, pipe_segment_ref])
                    else:
                        print(f"<A_002> section not found in {ptdx_file_path}")

                except ET.ParseError as e:
                    print(f"Error: Invalid XML in {ptdx_file_path} - {e}")
                except Exception as ex:
                    print(f"Unexpected error processing {ptdx_file_path}: {ex}")

    # Save the workbook to the specified Excel file path
    workbook.save(excel_file_path)
    print(f"Data extracted and saved to {excel_file_path}")

# Replace the paths with your actual folder and output file path
project_folder = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\Inspections"  # Example: "C:/Projects/YourProjectFolder"
output_excel_file = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\completeRatings.xlsx"  # Example: "C:/Projects/ExtractedData.xlsx"
extract_to_excel(project_folder, output_excel_file)
