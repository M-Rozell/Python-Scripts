import os
import xml.etree.ElementTree as ET
from openpyxl import Workbook

def detect_value_type(value):
    """Detect whether a value is an integer, float, or text."""
    try:
        int(value)
        return "Integer"
    except ValueError:
        try:
            float(value)
            return "Float"
        except ValueError:
            return "Text"

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
    sheet.append(["File Name", "Upstream_AP", "Upstream_AP Type", 
                  "Downstream_AP", "Downstream_AP Type", 
                  "Pipe_Segment_Reference", "Pipe_Segment_Reference Type", "WorkOrder", "WorkOrder Type", "Purpose", "Purpose Type"])

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ptdX"):  # Look for .ptdx files
                ptdx_file_path = os.path.join(root, file)
                try:
                    # Parse the .ptdx file as XML
                    print(f"Processing: {ptdx_file_path}")
                    tree = ET.parse(ptdx_file_path)
                    root_element = tree.getroot()

                    # Extract the values from <A_002>
                    i_002 = root_element.find(".//I_002")
                    if i_002 is not None:
                        upstream_ap = i_002.find("Upstream_AP").text if i_002.find("Upstream_AP") is not None else ""
                        downstream_ap = i_002.find("Downstream_AP").text if i_002.find("Downstream_AP") is not None else ""
                        pipe_segment_ref = i_002.find("Pipe_Segment_Reference").text if i_002.find("Pipe_Segment_Reference") is not None else ""
                        workorder = i_002.find("WorkOrder").text if i_002.find("WorkOrder") is not None else ""
                        purpose = i_002.find("Purpose").text if i_002.find("Purpose") is not None else ""

                        # Detect types of the values
                        upstream_ap_type = detect_value_type(upstream_ap)
                        downstream_ap_type = detect_value_type(downstream_ap)
                        pipe_segment_ref_type = detect_value_type(pipe_segment_ref)
                        workorder_type = detect_value_type(workorder)
                        purpose_type = detect_value_type(purpose)

                        # Append the extracted data and types to the Excel file
                        sheet.append([file, upstream_ap, upstream_ap_type, 
                                      downstream_ap, downstream_ap_type, 
                                      pipe_segment_ref, pipe_segment_ref_type, workorder_type, purpose_type])
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
output_excel_file = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\Ratings.xlsx"  # Example: "C:/Projects/ExtractedData.xlsx"
extract_to_excel(project_folder, output_excel_file)
