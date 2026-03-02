import foremka as frm

if __name__ == "__main__":
    foremki = [frm.ForemkaProstokatna("stal",40,60), frm.ForemkaOkragla("drewno", 50), frm.ForemkaTrojkatna("plastik",50)]
    for foremka in foremki:
        print(foremka.opis())
        print("pole:", round(foremka.pole(), 2))
        print("obwod:", round(foremka.obwod(), 2))
        print("ile ciastek z blachy 300×200 mm:", foremka.ile_ciastek(300, 200))