from math import pi, sqrt

def total_surface_area(r, h):
    """Funkcja do obliczania pola stożka"""
    s = sqrt(pow(r, 2) + pow(h, 2))
    return pi * pow(r, 2) + pi * r * s

def volume(r, h):
    """Funkcja do obliczania objętości stożka"""
    return pi * pow(r,2) * h / 3

if __name__ == '__main__':
    try:
        while True:
            selection = int(input("Wybierz pole (1) lub objętość (2): "))
            if selection == 1:
                r1 = float(input("Wpisz promień: "))
                h1 = float(input("Wpisz wysokość: "))
                print(f"Pole wynosi: {total_surface_area(r1, h1)}")
                break
            elif selection == 2:
                r1 = float(input("Wpisz promień: "))
                h1 = float(input("Wpisz wysokość: "))
                print(f"Objętość wynosi: {volume(r1, h1)}")
                break
    except Exception as e:
        print(f"Wystąpił błąd:\n{e}")
