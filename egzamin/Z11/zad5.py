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

    yield from all_divisors


print("2. Dzielniki liczby 36:")
for div in divisors(36):
    print(div, end=" ")
print("\n")

NUMBER_TO_CHECK = 17

divisors_list = list(divisors(NUMBER_TO_CHECK))
is_prime = len(divisors_list) == 2

print(f"3. Sprawdzanie liczby {NUMBER_TO_CHECK}:")
print(f"Wszystkie dzielniki: {divisors_list}")
print(f"Czy liczba {NUMBER_TO_CHECK} jest pierwsza? {is_prime}")
