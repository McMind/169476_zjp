class Foremka:
    def __init__(self, material: str, ksztalt: str):
        self.material = material
        self.ksztalt = ksztalt

    def pole(self) -> float:
        "Pole foremki"

    def obwod(self) -> float:
        "Obwód foremki"

    def wykroj(self) -> str:
        return "Wykrojono kawałek ciasta"

    def opis(self) -> str:
        return f"Materiał: {self.material}, Kształt: {self.ksztalt}"

    def ile_ciastek(self, szerokosc_ciasta_mm: int | float, dlugosc_ciasta_mm: int
                                                                               | float) -> int:
        pole_ciasta = szerokosc_ciasta_mm * dlugosc_ciasta_mm
        return int(pole_ciasta // self.pole())
