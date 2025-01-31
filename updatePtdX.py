import os
import xml.etree.ElementTree as ET

def validate_and_modify_ptdx(folder_path):
    # Ensure the provided folder path exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ptdX"):  # Look for .ptdx files
                ptdx_file_path = os.path.join(root, file)
                try:
                    # Parse the .ptdx file as XML
                    print(f"Processing: {ptdx_file_path}")
                    tree = ET.parse(ptdx_file_path)  # Validate XML structure
                    root_element = tree.getroot()

                    # Modify <Material> element if its value is "ZZZ"
                    for material in root_element.findall(".//A_002/Material"):
                        if material.text == "ZZZ":
                            material.text = "XXX"
                            print(f"Updated Material to 'XXX' in {ptdx_file_path}")

                    # Modify <Owner> element 
                    for owner in root_element.findall(".//A_002/Owner"):
                            owner.text = "Jefferson County"
                            print(f"Updating Owner in {ptdx_file_path}")

                    # Modify <Customer> element 
                    for customer in root_element.findall(".//I_002/Customer"):
                            customer.text = "Jefferson County"
                            print(f"Updating Customer in {ptdx_file_path}")

                    # Modify <PO_Number> element 
                    for poNumber in root_element.findall(".//I_002/PO_Number"):
                            poNumber.text = " "
                            print(f"Updating PO_Number in {ptdx_file_path}")

                    # Modify <Project> element 
                    for project in root_element.findall(".//I_002/Project"):
                            project.text = "2024 AMP06"
                            print(f"Updating Project in {ptdx_file_path}")

                    # Modify WorkOrder in <I_002>
                    for work_order in root_element.findall(".//I_002/WorkOrder"):
                        work_order.text = "017560-17"
                        print(f"Updated WorkOrder to '017560-17' in {ptdx_file_path}")

                    # Modify Purpose in <I_002>
                    for purpose in root_element.findall(".//I_002/Purpose"):
                        purpose.text = "G"
                        print(f"Updated Purpose to 'G' in {ptdx_file_path}")

                    # Modify Inspection_Technology_Used_CCTV in <I_002>
                    for cctv in root_element.findall(".//I_002/Inspection_Technology_Used_CCTV"):
                        cctv.text = "true"
                        print(f"Updated Inspection_Technology_Used_CCTV to 'true' in {ptdx_file_path}")
                            

                    # Check if <Code>MSA</Code> exists
                    msa_exists = any(code.text == "MSA" for code in root_element.findall(".//Code"))

                    if not msa_exists:
                        # Find <Total_Length> and <Length_Surveyed>
                        total_length = root_element.find(".//A_002/Total_Length")
                        length_surveyed = root_element.find(".//I_002/Length_Surveyed")

                        if total_length is not None and length_surveyed is not None:
                            # Update <Total_Length> value
                            print(f"Updating Total_Length in {ptdx_file_path} from {total_length.text} to {length_surveyed.text}")
                            total_length.text = length_surveyed.text
                        else:
                            print(f"Missing required tags in {ptdx_file_path}")

                    

                    # Save the updated tree back to the original .ptdx file
                    tree.write(ptdx_file_path, encoding="utf-8", xml_declaration=True)
                    print(f"Updated and saved: {ptdx_file_path}")
                except ET.ParseError as e:
                    print(f"Error: Invalid XML in {ptdx_file_path} - {e}")
                except Exception as ex:
                    print(f"Unexpected error processing {ptdx_file_path}: {ex}")

# Replace 'your_project_folder_path' with your actual project folder path
project_folder = r"C:\Users\MaggieRozell\Desktop\Trash\Ratings\Inspections"  # Example: "C:/Projects/YourProjectFolder"
validate_and_modify_ptdx(project_folder)
