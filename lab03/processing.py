from table import SimpleTable

import math


def _lp_norm(vector, p):
    """Oblicza normę Lp dla wektora."""
    if p < 1:
        raise ValueError("p must be >= 1.")

    sum_pow = sum(abs(x) ** p for x in vector)
    return sum_pow ** (1 / p)


class Preprocessing:
    __slots__ = ['__data']

    def __init__(self, data: SimpleTable) -> None:
        if not isinstance(data, SimpleTable):
            raise ValueError("Data must be a SimpleTable type.")
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.deleter
    def data(self):
        """Czyści tabelę, wstawiając 0 w każde miejsce."""
        raw_data = self.__data.data
        for r in range(len(raw_data)):
            for c in range(len(raw_data[r])):
                raw_data[r][c] = 0

    def _get_vectors(self, axis):
        """Pomocnicza metoda do wyciągania wierszy lub kolumn."""
        if axis.lower() == 'row':
            return [row for row in self.__data.data]
        elif axis.lower() == 'col':
            rows, cols = self.__data.shape
            return [[self.__data.data[r][c] for r in range(rows)] for c in range(cols)]
        else:
            raise ValueError("Parameter axis only takes values: 'col' or 'row'.")

    def _set_vectors(self, axis, vectors):
        """Pomocnicza metoda do zapisywania przeliczonych danych z powrotem."""
        if axis == 'row':
            for r in range(len(vectors)):
                self.__data.data[r] = vectors[r]
        elif axis == 'col':
            rows, cols = self.__data.shape
            for c in range(cols):
                for r in range(rows):
                    self.__data.data[r][c] = vectors[c][r]

    def normalize(self, axis, p: float | int = 2) -> None:
        """Normalizacja wektorowa przy użyciu normy Lp. Domyślnie p=2 (norma Euklidesowa)."""
        vectors = self._get_vectors(axis)
        new_vectors = []

        for v in vectors:
            norm = _lp_norm(v, p)
            new_vectors.append([x / norm if norm > 0 else 0 for x in v])

        self._set_vectors(axis, new_vectors)

    def min_max_scaling(self, axis: str) -> None:
        """Skalowanie do przedziału [0, 1]."""
        vectors = self._get_vectors(axis)
        new_vectors = []
        for v in vectors:
            v_min, v_max = min(v), max(v)
            diff = v_max - v_min
            new_vectors.append([(x - v_min) / diff if diff > 0 else 0 for x in v])
        self._set_vectors(axis, new_vectors)

    def standardize(self, axis: str) -> None:
        """Standaryzacja (z-score): (x - mean) / std_dev."""
        vectors = self._get_vectors(axis)
        new_vectors = []
        for v in vectors:
            mean = sum(v) / len(v) if v else 0
            variance = sum((x - mean) ** 2 for x in v) / len(v) if v else 0
            std_dev = math.sqrt(variance)
            new_vectors.append([(x - mean) / std_dev if std_dev > 0 else 0 for x in v])
        self._set_vectors(axis, new_vectors)

    def __repr__(self):
        return f"Preprocessing(data={self.data!r})"

    def __str__(self):
        return f"Preprocessing:\n{self.data}"


if __name__ == "__main__":
    obj1 = Preprocessing(SimpleTable([[1, 2, 3], [5, 7, 9], [11, 12, 13]]))
    print(obj1)
    obj1.data.add_row([3, 4, 1])
    print(obj1)
    obj1.normalize('col', 1.5)
    print(obj1)
    del obj1.data
    print(obj1)
