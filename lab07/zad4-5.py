from faker import Faker
import random

if __name__ == '__main__':
    Faker.seed(39)
    fake = Faker()
    lista_imion = [fake.name() for _ in range(100)]
    lista_ocen = random.choices(range(3,6), k=100)
    wynik = zip(lista_imion, lista_ocen)
    print(list(wynik))
    # zad 5
    wedlug_ocen = sorted(zip(lista_imion, lista_ocen), key=lambda x: x[1], reverse=True)
    print(list(wedlug_ocen))
