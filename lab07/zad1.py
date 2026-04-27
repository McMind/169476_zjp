if __name__ == '__main__':
    lista1 = [1, 2, 3, 4, 5]
    kwadraty = lambda x : pow(x, 2)
    szesciany = lambda x : pow(x, 3)
    print(list(map(kwadraty, lista1)))
    print(list(map(szesciany, lista1)))