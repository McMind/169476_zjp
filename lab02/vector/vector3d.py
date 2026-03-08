from math import sqrt, degrees, acos

from vector.vector2d import Vector2D


class Vector3D(Vector2D):

    def __init__(self, x: int|float, y: int|float, z: int|float) -> None:
        super().__init__(x, y)
        self.z = z

    def __abs__(self) -> float:
        """Zwraca długość wektora 3D"""
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __len__(self) -> int:
        return 3

    def __gt__(self, other: Vector3D) -> bool:
        return abs(self) > abs(other)

    def __ge__(self, other: Vector3D) -> bool:
        return abs(self) >= abs(other)

    def __lt__(self, other: Vector3D) -> bool:
        return abs(self) < abs(other)

    def __le__(self, other: Vector3D) -> bool:
        return abs(self) <= abs(other)

    def __ne__(self, other: Vector3D) -> bool:
        return abs(self) != abs(other)

    def __eq__(self, other: Vector3D) -> bool:
        return abs(self) == abs(other)

    def __bool__(self) -> bool:
        return abs(self).__bool__()

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def normalize(self) -> Vector3D:
        """Zwraca wektor znormalizowany"""
        mag = abs(self)
        if mag == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def dot_product(self, other: Vector3D) -> float:
        """Zwraca iloczyn skalarny"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle_between(self, other: Vector3D) -> float:
        """Zwraca kąt w stopniach między wektorem klasy bazowej, a podanym w funkcji"""
        mags = abs(self) * abs(other)
        if mags == 0:
            return -1
        cos_theta = self.dot_product(other) / mags
        return degrees(acos(cos_theta))