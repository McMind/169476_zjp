from math import sqrt, degrees, acos


class Vector2D:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y

    def __abs__(self) -> float:
        """Zwraca długość wektora"""
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __len__(self) -> int:
        return 2

    def __gt__(self, other: Vector2D) -> bool:
        return abs(self) > abs(other)

    def __ge__(self, other: Vector2D) -> bool:
        return abs(self) >= abs(other)

    def __lt__(self, other: Vector2D) -> bool:
        return abs(self) < abs(other)

    def __le__(self, other: Vector2D) -> bool:
        return abs(self) <= abs(other)

    def __ne__(self, other: Vector2D) -> bool:
        return abs(self) != abs(other)

    def __eq__(self, other: Vector2D) -> bool:
        return abs(self) == abs(other)

    def __bool__(self) -> bool:
        return abs(self).__bool__()

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def normalize(self) -> Vector2D:
        """Zwraca wektor znormalizowany"""
        mag = abs(self)
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)

    def dot_product(self, other: Vector2D) -> float:
        """Zwraca iloczyn skalarny"""
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: Vector2D) -> float:
        """Zwraca kąt w stopniach między wektorem klasy bazowej, a podanym w funkcji"""
        mags = abs(self) * abs(other)
        if mags == 0:
            return -1
        cos_theta = self.dot_product(other) / mags
        return degrees(acos(cos_theta))
