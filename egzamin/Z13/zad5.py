def digits(n):
    list1 = []
    while n > 0:
        list1.append(n % 10)
        n //= 10

    list1 = list(reversed(list1))
    yield from list1


print(list(digits(78652)))

result2 = list(digits(12345))
sum_result2 = sum(result2)
if sum_result2 % 3 == 0:
    print("12345 jest podzielne przez 3")
else:
    print("12345 nie jest podzielne przez 3")
