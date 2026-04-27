from faker import Faker

if __name__ == '__main__':
    Faker.seed(39)
    fake = Faker()
    lista_imion = [fake.name() for _ in range(1000)]
    wedlug_dlugosci = sorted(lista_imion, key=lambda imie: len(imie))
    print(wedlug_dlugosci)