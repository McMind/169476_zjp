def fibonacci_up_to_n(n):
    list1 = [0, 1]
    while (list1[-1] + list1[-2]) < n:
        list1.append(list1[-1] + list1[-2])

    yield from list1


print(list(fibonacci_up_to_n(100)))
