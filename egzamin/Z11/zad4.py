class Vector2D:

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        if scalar == 0:
            raise ZeroDivisionError("Nie można dzielić wektora przez zero.")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"



v = Vector2D(3, 4)
print(f"Wektor bazowy: {v}\n")

result_mul = v * 2
print(f"v * 2   -> {result_mul}")

result_rmul = 0.5 * v
print(f"0.5 * v -> {result_rmul}")

result_div = v / 4
print(f"v / 4   -> {result_div}")

try:
    v / 0
except ZeroDivisionError as e:
    print(f"\nBłąd: {e}")