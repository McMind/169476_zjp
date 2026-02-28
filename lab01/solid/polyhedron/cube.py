
def total_surface_area(a):
    """Funkcja do obliczania pola sześcianu"""
    return 6 * pow(a,2)

def volume(a):
    """Funkcja do obliczania objętości sześcianu"""
    return pow(a,3)

if __name__ == '__main__':
    try:
        while True:
            selection = int(input("Wybierz pole (1) lub objętość (2): "))
            if selection == 1:
                a1 = float(input("Wpisz bok: "))
                print(f"Pole wynosi: {total_surface_area(a1)}")
                break
            elif selection == 2:
                a1 = float(input("Wpisz bok: "))
                print(f"Objętość wynosi: {volume(a1)}")
                break
    except Exception as e:
        print(f"Wystąpił błąd:\n{e}")
