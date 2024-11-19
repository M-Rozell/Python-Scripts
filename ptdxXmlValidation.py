import os
import xml.etree.ElementTree as ET



def validate_and_convert_ptdx(folder_path):
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
                            print(f"Updating Material in {ptdx_file_path}")
                            material.text = "XXX"
                            
                    # Save as .xml in the same folder
                    xml_file_name = ".xml"
                    xml_file_path = os.path.join(root, xml_file_name)
                    tree.write(xml_file_path, encoding="utf-8", xml_declaration=True)
                    
                    print(f"Saved as: {xml_file_path}")
                except ET.ParseError as e:
                    print(f"Error: Invalid XML in {ptdx_file_path} - {e}")
                except Exception as ex:
                    print(f"Unexpected error processing {ptdx_file_path}: {ex}")

# Replace 'your_project_folder_path' with your actual project folder path
project_folder = r"C:\Users\MaggieRozell\Desktop\Trash\Actual Trash\Other"  # Example: "C:/Projects/YourProjectFolder"
validate_and_convert_ptdx(project_folder)

