import xml.etree.ElementTree as ET

if __name__ == '__main__':

    tree = ET.parse("biblioteka.xml")
    root = tree.getroot()

    print("(a) Wszystkie tytuły:")

    for ksiazka in root.findall("ksiazka"):
        tytul = ksiazka.find("tytul").text
        print(tytul)

    print("-"*40)

    print("(b) Tylko książki z kategori informatyka:")

    for ksiazka in root.findall("ksiazka"):
        if ksiazka.find("kategoria").text != "informatyka":
            continue
        tytul = ksiazka.find("tytul").text
        autor = ksiazka.find("autor").text
        rok = ksiazka.find("rok").text
        kategoria = ksiazka.find("kategoria").text
        print(tytul, autor, rok, kategoria)

    print("(c) Dodanie nowej książki")

    nowa_ksiazka = ET.Element("ksiazka")
    nowa_ksiazka.set("id", "4")

    nowy_tytul = ET.SubElement(nowa_ksiazka, "tytul")
    nowy_tytul.text = "Harry Potter"

    nowy_autor = ET.SubElement(nowa_ksiazka, "autor")
    nowy_autor.text = "J. K. Rowling"

    nowy_rok = ET.SubElement(nowa_ksiazka, "rok")
    nowy_rok.text = "2005"

    nowa_kategoria = ET.SubElement(nowa_ksiazka, "kategoria")
    nowa_kategoria.text = "fantastyka"

    root.append(nowa_ksiazka)

    print("(c1) Książka dodana")

    print("(d) Zmiana roku książki o id=1 na 2026")

    for ksiazka in root.findall("ksiazka"):

        if ksiazka.get("id") == "1":
            ksiazka.find("rok").text = "2026"
            break

    print("(e) Zapis do pliku biblioteka_zmieniona.xml")

    tree.write("biblioteka_zmieniona.xml", encoding="utf-8", xml_declaration=True)
