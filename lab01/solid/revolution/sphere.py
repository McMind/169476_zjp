from math import pi

def total_surface_area(r):
    """Funkcja do obliczania pola kuli"""
    return 4 * pi * pow(r, 2)

def volume(r):
    """Funkcja do obliczania objętości kuli"""
    return 4 * pi * pow(r, 3) / 3

if __name__ == '__main__':
    try:
        while True:
            selection = int(input("Wybierz pole (1) lub objętość (2): "))
            if selection == 1:
                r1 = float(input("Wpisz promień: "))
                print(f"Pole wynosi: {total_surface_area(r1)}")
                break
            elif selection == 2:
                r1 = float(input("Wpisz promień: "))
                print(f"Objętość wynosi: {volume(r1)}")
                break
    except Exception as e:
        print(f"Wystąpił błąd:\n{e}")
