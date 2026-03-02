from math import pi
from foremka import Foremka


class ForemkaOkragla(Foremka):
    def __init__(self, material: str, srednica_mm: float):
        super().__init__(material, "okrąg")
        self.srednica_mm = srednica_mm

    def pole(self) -> float:
        r = self.srednica_mm / 2
        return pi * r ** 2

    def obwod(self) -> float:
        return pi * self.srednica_mm

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}, Średnica: {self.srednica_mm} mm"
