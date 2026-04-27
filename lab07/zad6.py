if __name__ == '__main__':
    lista_procentow = tuple(range(0,101))
    lista_ocen = (2, 3, 3.5, 4, 4.5, 5)
    progi_procentowe = (60, 69, 77, 86, 95)
    progi = lambda procent: lista_ocen[sum(p <= procent for p in progi_procentowe)]
    wynik = map(progi, lista_procentow)
    porownanie = zip(lista_procentow, wynik)
    print(list(porownanie))