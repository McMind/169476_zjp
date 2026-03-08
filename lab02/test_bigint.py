from bigint import BigInt


def test_bigint():
    print("--- Testy Konstruktora i Reprezentacji ---")
    print(f"Dodatnia: {BigInt('123')}")
    print(f"Ujemna:   {BigInt('-456')}")
    print(f"Zero:     {BigInt('-000')}")

    print("\n--- Testy Porównywania ---")
    a, b, c = BigInt("10"), BigInt("-10"), BigInt("10")
    print(f"10 == 10:   {a == c}")  # True
    print(f"10 > -10:   {a > b}")  # True
    print(f"-10 < 10:   {b < a}")  # True
    print(f"-10 == 10:  {b == a}")  # False

    print("\n--- Testy Dodawania i Odejmowania ---")
    # 100 + (-40) = 60
    print(f"100 + (-40) = {BigInt('100') + BigInt('-40')}")
    # 30 - 100 = -70
    print(f"30 - 100    = {BigInt('30') - BigInt('100')}")
    # -50 - 50 = -100
    print(f"-50 - 50    = {BigInt('-50') - BigInt('50')}")
    # -10 - (-30) = 20
    print(f"-10 - (-30) = {BigInt('-10') - BigInt('-30')}")

    print("\n--- Testy Mnożenia ---")
    m1 = BigInt("123456789")
    m2 = BigInt("-10")
    print(f"123456789 * -10: {m1 * m2}")  # -1234567890
    print(f"0 * -5:          {BigInt('0') * BigInt('-5')}")  # 0

    print("\n--- Testy Operatorów Przypisania ---")
    val = BigInt("500")
    val += BigInt("500")
    print(f"500 += 500: {val}")
    val *= BigInt("-1")
    print(f"1000 *= -1: {val}")

    print("\n--- Test Bardzo Dużych Liczb ---")
    big = BigInt("9" * 30)
    one = BigInt("1")
    print(f"Wielka liczba + 1: {big + one}")


if __name__ == "__main__":
    try:
        test_bigint()
    except Exception as e:
        print(f"\nWystąpił problem: {e}")