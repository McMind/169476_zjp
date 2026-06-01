import math


def divisors(n: int):
    if n <= 0:
        raise ValueError("Liczba musi być dodatnia.")

    left_divisors = []
    right_divisors = []

    limit = int(math.isqrt(n))

    for i in range(1, limit + 1):
        if n % i == 0:
            left_divisors.append(i)
            if i != n // i:
                right_divisors.append(n // i)

    all_divisors = left_divisors + right_divisors[::-1]

    for d in all_divisors:
        yield d

print("2. Dzielniki liczby 36:")
for div in divisors(36):
    print(div, end=" ")
print("\n")

number_to_check = 17

divisors_list = list(divisors(number_to_check))
is_prime = len(divisors_list) == 2

print(f"3. Sprawdzanie liczby {number_to_check}:")
print(f"Wszystkie dzielniki: {divisors_list}")
print(f"Czy liczba {number_to_check} jest pierwsza? {is_prime}")