import os
import xml.etree.ElementTree as ET

def validate_and_modify_ptdx(folder_path):

    files_changed = 0

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
                            files_changed += 1
                            print(f"Updating Material in {ptdx_file_path}")
                            material.text = "XXX"

                    # Save the updated tree back to the original .ptdx file
                    tree.write(ptdx_file_path, encoding="utf-8", xml_declaration=True)
                    print(f"Updated and saved: {ptdx_file_path}")
                except ET.ParseError as e:
                    print(f"Error: Invalid XML in {ptdx_file_path} - {e}")
                except Exception as ex:
                    print(f"Unexpected error processing {ptdx_file_path}: {ex}")
    print(f" {files_changed} files have been changed")
                   

# Replace 'your_project_folder_path' with your actual project folder path
project_folder = r"Z:\017560-12 - JEFFCO 2022 AMP08 - MAINLINE\Upgrade\2022\06\Other\Structural"  # Example: "C:/Projects/YourProjectFolder"
validate_and_modify_ptdx(project_folder)
