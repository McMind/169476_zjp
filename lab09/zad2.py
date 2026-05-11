import xml.etree.ElementTree as ET

if __name__ == '__main__':

    tree = ET.parse("studenci.xml")
    root = tree.getroot()

    for student in root.findall("student"):
        if student.find("kierunek").text != 'informatyka':
            continue
        imie = student.find("imie").text
        nazwisko = student.find("nazwisko").text
        wiek = student.find("wiek").text
        kierunek = student.find("kierunek").text

        print(imie, nazwisko, wiek, kierunek)