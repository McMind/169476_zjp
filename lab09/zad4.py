import xml.etree.ElementTree as ET

if __name__ == '__main__':

    tree = ET.parse("studenci.xml")
    root = tree.getroot()

    for student in root.findall("student"):

        if student.get("id") == "1":
            student.find("wiek").text = "26"
    
    tree.write("studenci_zmienieni.xml", encoding="utf-8", xml_declaration=True)