def list_divisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i

result1 = list(list_divisors(36))
print(result1)