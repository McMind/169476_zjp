import random

if __name__ == '__main__':
    random.seed(39)
    lista_generowana = random.choices(range(0,101), k=pow(10,5))
    podzielne = filter(lambda x: x % 10 == 0, lista_generowana)
    print(list(podzielne))