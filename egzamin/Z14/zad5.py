def fibonacci_up_to_n(n):
    list1 = [0, 1]
    while (list1[-1] + list1[-2]) < n:
        list1.append(list1[-1] + list1[-2])

    for element in list1:
        yield element

print(list(fibonacci_up_to_n(100)))