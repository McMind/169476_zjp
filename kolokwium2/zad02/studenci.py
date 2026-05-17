studenci = [
    ("Anna", "Kowalska", 91),
    ("Jan", "Nowak", 64),
    ("Ola", "Wiśniewska", 78),
    ("Piotr", "Zieliński", 45),
    ("Maria", "Wójcik", 100),
    ("Tomasz", "Lewandowski", 33),
]

lista_ocen = (2, 3, 3.5, 4, 4.5, 5)
progi_procentowe = (50, 65, 75, 85, 95)
progi = lambda procent: lista_ocen[sum(p <= procent for p in progi_procentowe)]

""" (a)
 wyznaczanie ocen za pomocą map() i lambda
"""

lista_procentow = [student[2] for student in studenci]
oceny = list(map(progi, lista_procentow))

""" (b)
 filtrowanie studentów, którzy zdali (>= 50%) za pomocą filter()
"""

zaliczyli = list(filter(lambda student: student[2] >= 50, studenci))

""" (c)
 sortowanie malejąco według punktów za pomocą sorted()
"""

posortowani = sorted(studenci, key=lambda student: student[2], reverse=True)
""" (d)
 listy par ("imię nazwisko", ocena) za pomocą zip()
"""

imie_nazwisko_lista = [f"{s[0]} {s[1]}" for s in studenci]

pary_student_ocena = list(zip(imie_nazwisko_lista, oceny))

if __name__ == '__main__':
    print("a. Obliczone oceny dla kolejnych punktów")
    print(f"Punkty: {lista_procentow}")
    print(f"Oceny:  {oceny}")
    print("-"*40)

    print("b. Studenci, którzy zaliczyli (punkty >= 50)")
    print(zaliczyli)
    print("-"*40)

    print("c. Studenci posortowani malejąco według punktów")
    print(posortowani)
    print("-"*40)

    print("d. Pary ('Imię Nazwisko', ocena)")
    print(pary_student_ocena)
