import xml.etree.ElementTree as ET

if __name__ == '__main__':

    tree = ET.parse("studenci.xml")
    root = tree.getroot()

    for student in root.findall("student"):
        if student.get("id") != "2":
            continue
        root.remove(student)
        break

    tree.write("studenci_usuniety.xml", encoding="utf-8", xml_declaration=True)
