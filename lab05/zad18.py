def parzyste_gen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

if __name__ == '__main__':
    for p in parzyste_gen(10):
        print(p)