from foremka import Foremka


class ForemkaProstokatna(Foremka):

    def __init__(self, material: str, a_mm: float, b_mm: float):
        super().__init__(material, "prostokąt")
        self.a_mm = a_mm
        self.b_mm = b_mm

    def pole(self) -> float:
        return self.a_mm * self.b_mm

    def obwod(self) -> float:
        return 2 * (self.a_mm + self.b_mm)

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}, Wymiary: {self.a_mm}×{self.b_mm} mm"
