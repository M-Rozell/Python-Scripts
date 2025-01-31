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


                    # Access <A_002> section
                    a_002 = root_element.find(".//A_002")

                    # Ensure <Lining_Method> exists and update
                    lining_method = a_002.find("Lining_Method")
                    if lining_method is None:
                            lining_method = ET.SubElement(a_002, "Lining_Method")
                            print("Created missing <Lining_Method> tag.")
     
                    
                    
                    # Modify <Lining_Method> element if value is not "CP"
                    update_lining_method = a_002.find("Lining_Method")
                    for material in root_element.findall(".//A_002/Material"):
                         if material.text == "XXX":
                            update_lining_method.text = "CP"
                            print("Lining_Method updated")
                         else:
                             a_002.remove(update_lining_method)
                             print("Removed <Lining_Method>") 
                         
                    

                    # Remove <Lining_Method> element if value is not "CP"
                    #for a_002 in root_element.findall(".//A_002"):
                        #lining_method = a_002.find("Lining_Method")
                        #if lining_method.text != "CP":
                           #a_002.remove(lining_method)
                           #print("Removed <Lining_Method>")      
                    
                        
  

                    # Save the updated tree back to the original .ptdx file
                    tree.write(ptdx_file_path, encoding="utf-8", xml_declaration=True)
                    print(f"Updated and saved: {ptdx_file_path}")
                except ET.ParseError as e:
                    print(f"Error: Invalid XML in {ptdx_file_path} - {e}")
                except Exception as ex:
                    print(f"Unexpected error processing {ptdx_file_path}: {ex}")

                    

# Replace 'your_project_folder_path' with your actual project folder path
project_folder = r"C:\Users\MaggieRozell\Desktop\Trash\Update Practice"  # Example: "C:/Projects/YourProjectFolder"
validate_and_modify_ptdx(project_folder)