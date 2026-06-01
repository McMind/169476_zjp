class Product:

    def __init__(self, name: str, base_price: float, discount: float = 0):
        self.name = name
        self.base_price = base_price
        self.discount = discount

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            raise ValueError("Nazwa produktu nie może być pusta.")
        self._name = str(value).strip()

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Cena bazowa musi być liczbą dodatnią.")
        self._base_price = float(value)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, (int, float)) or not (0 <= value <= 100):
            raise ValueError("Rabat musi mieścić się w przedziale od 0 do 100.")
        self._discount = float(value)

    @property
    def final_price(self):
        price_after_discount = self.base_price * (1 - self.discount / 100)
        return round(price_after_discount, 2)

    def __str__(self):
        return f"Produkt: {self.name} | Cena końcowa: {self.final_price:.2f} zł (Rabat: {self.discount}%)"



print("=== Test 1: Poprawne działanie ===")
prod = Product("Laptop", 3500.00, 10)
print(prod)
print(f"Cena końcowa na start: {prod.final_price} zł")

prod.discount = 25
print(f"Cena po zmianie rabatu na 25%: {prod.final_price} zł")
print(prod)

print("\n=== Test 2: Obsługa błędnych wartości ===")

try:
    prod.name = ""
except ValueError as e:
    print(f"Błąd nazwy: {e}")

try:
    prod.base_price = -10
except ValueError as e:
    print(f"Błąd ceny: {e}")

try:
    prod.discount = 120
except ValueError as e:
    print(f"Błąd rabatu: {e}")

try:
    invalid_prod = Product("Telefon", 1500, -5)
except ValueError as e:
    print(f"Błąd podczas tworzenia obiektu: {e}")