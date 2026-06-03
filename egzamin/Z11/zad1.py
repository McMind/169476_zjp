def process_numbers(numbers: list[int], condition, transform) -> list[int]:
    return [transform(num) for num in numbers if condition(num)]


data = [-5, -2, 0, 3, 7, 10, 15, 22]

print(f"Lista startowa: {data}\n")

result_1 = process_numbers(data, lambda x: x > 0, lambda x: x ** 2)
print(f"1. Kwadraty liczb dodatnich: {result_1}")

result_2 = process_numbers(data, lambda x: x < 0, lambda x: abs(x) + 100)
print(f"2. Abs liczb ujemnych + 100: {result_2}")

result_3 = process_numbers(data, lambda x: x % 2 == 0, lambda x: x // 2)
print(f"3. Liczby parzyste podzielone przez 2: {result_3}")

result_4 = process_numbers(data, lambda x: 1 <= x <= 10, lambda x: x)
print(f"4. Liczby od 1 do 10: {result_4}")
