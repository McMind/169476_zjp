class Recipe:
    def __init__(self, flour, sugar, butter):
        self.flour = flour
        self.sugar = sugar
        self.butter = butter

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Recipe(self.flour * other, self.sugar * other, self.butter * other)

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Recipe(other * self.flour, other * self.sugar, other * self.butter)

    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("Wykryto dzielenie przez 0")
        return Recipe(self.flour / other, self.sugar / other, self.butter / other)

    def __repr__(self):
        return f"Recipe({self.flour:.2f}, {self.sugar:.2f}, {self.butter:.2f})"


if __name__ == "__main__":
    r = Recipe(500, 200, 100)
    print(f"r => {r}")
    print(f"r * 2 => {r * 2}")
    print(f"0.5 * r => {0.5 * r}")
    print(f"r / 4 => {r / 4}")
