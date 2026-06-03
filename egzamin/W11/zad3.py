class HotelRoom:
    def __init__(self, room_name, base_night_price, seasonal_discount=0):
        self.room_name = room_name
        self.base_night_price = base_night_price
        self.seasonal_discount = seasonal_discount

    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, new_room_name):
        if new_room_name is None or new_room_name.strip() == "":
            raise ValueError("Nazwa nie może być pusta")
        self._room_name = new_room_name

    @property
    def base_night_price(self):
        return self._base_night_price

    @base_night_price.setter
    def base_night_price(self, new_base_night_price):
        if new_base_night_price <= 0:
            raise ValueError("Cena musi być liczbą dodatnią")
        self._base_night_price = new_base_night_price

    @property
    def seasonal_discount(self):
        return self._seasonal_discount

    @seasonal_discount.setter
    def seasonal_discount(self, new_seasonal_discount):
        if not 0 <= new_seasonal_discount <= 100:
            raise ValueError("Zniżka musi mieścić się w przedziale 0 do 100 (włącznie)")
        self._seasonal_discount = new_seasonal_discount

    @property
    def final_night_price(self):
        return round((1 - self.seasonal_discount / 100) * self.base_night_price, 2)

    def __str__(self):
        return (f"Nazwa: {self.room_name}, Cena bazowa: ${self.base_night_price:.2f}, "
                f"Zniżka {self.seasonal_discount:.2f}%, Cena końcowa ${self.final_night_price:.2f}")


if __name__ == "__main__":
    print("Utworzenie pokoju")
    obj1 = HotelRoom("Pokój1", 3000)
    print(obj1)
    print("Zmiana zniżki")
    obj1.seasonal_discount = 7
    print(obj1)
    print("Wypisanie ceny końcowej")
    print(obj1.final_night_price)
    print("\nSprawdzanie błędnych wartości")
    try:
        obj1.room_name = ""
    except ValueError as e:
        print(e)
    try:
        obj1.base_night_price = 0
    except ValueError as e:
        print(e)
    try:
        obj1.seasonal_discount = 105
    except ValueError as e:
        print(e)
