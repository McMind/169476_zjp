import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse("studenci.xml")
    root = tree.getroot()

    nowy_student = ET.Element("student")
    nowy_student.set("id", "6")

    imie = ET.SubElement(nowy_student, "imie")
    imie.text = "Maria"

    nazwisko = ET.SubElement(nowy_student, "nazwisko")
    nazwisko.text = "Wesołowska"

    wiek = ET.SubElement(nowy_student, "wiek")
    wiek.text = "51"

    kierunek = ET.SubElement(nowy_student, "kierunek")
    kierunek.text = "prawo"

    root.append(nowy_student)
    tree.write("studenci_nowy.xml", encoding="utf-8", xml_declaration=True)