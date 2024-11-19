import os
import xml.etree.ElementTree as ET

def validate_and_modify_ptdx(folder_path):

    material_changed = 0

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
                    for material in root_element.findall(".//Material"):
                        if material.text == "ZZZ":
                            material_changed += 1
                            print(f"Updating Material in {ptdx_file_path}")
                            material.text = "XXX"

                     # Update <Total_Length> if <Code> is "AMH" or "AEP"
                    for of_002 in root_element.findall(".//OF_002"):
                        code = of_002.find("Code")
                        distance = of_002.find("Distance")
                        if code is not None and distance is not None and code.text in ["AMH", "AEP", "ACOH"]:
                            total_length = root_element.find(".//Total_Length")
                            if total_length is not None:
                                print(f"Updating Total_Length in {ptdx_file_path}: {distance.text}")
                                total_length.text = distance.text

                    # Save the updated tree back to the original .ptdx file
                    tree.write(ptdx_file_path, encoding="utf-8", xml_declaration=True)
                    print(f"Updated and saved: {ptdx_file_path}")
                except ET.ParseError as e:
                    print(f"Error: Invalid XML in {ptdx_file_path} - {e}")
                except Exception as ex:
                    print(f"Unexpected error processing {ptdx_file_path}: {ex}")
    print(f" {material_changed} files have been changed")
                   

# Replace 'your_project_folder_path' with your actual project folder path
project_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2022\06\Other\ProcedurealTip"  # Example: "C:/Projects/YourProjectFolder"
validate_and_modify_ptdx(project_folder)
