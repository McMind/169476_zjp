def kwadraty_gen(n):
    for i in range(1, n + 1):
        yield i ** 2

if __name__ == '__main__':
    print(list(kwadraty_gen(5)))