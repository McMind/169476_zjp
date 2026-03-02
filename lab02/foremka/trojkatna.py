from math import sqrt

from foremka import Foremka


class ForemkaTrojkatna(Foremka):
    def __init__(self, material: str, bok_mm: float):
        super().__init__(material, "trójkąt równoboczny")
        self.bok_mm = bok_mm

    def pole(self) -> float:
        return (self.bok_mm * self.bok_mm * sqrt(3)) / 4

    def obwod(self) -> float:
        return 3 * self.bok_mm

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}, Bok: {self.bok_mm} mm"
