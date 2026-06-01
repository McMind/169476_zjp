def multiples_up_to(n, limit):
    i = 1
    while n * i <= limit:
        yield n * i
        i += 1

result1 = list(multiples_up_to(7, 100))
print(result1)

if 84 in result1:
    print("84 jest wielokrotnością 7")
else:
    print("84 nie jest wielokrotnością 7")
