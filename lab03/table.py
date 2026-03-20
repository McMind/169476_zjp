from typing import Any


class SimpleTable:
    __slots__ = ['_data']

    def __init__(self, data: list[list[Any]]=None) -> None:
        if data is None:
            self._data = []
        else:
            if data and any(len(row) != len(data[0]) for row in data):
                raise ValueError("Expected rectangle list of lists.")
            self._data = [list(row) for row in data]

    @property
    def shape(self) -> tuple:
        """Zwraca wymiary tablicy."""
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0
        return rows, cols

    @property
    def data(self):
        return self._data

    @data.deleter
    def data(self):
        """Czyści tabelę do postaci listy pustej."""
        self._data = []

    def add_row(self, row: list[Any]) -> None:
        """Dodaje wiersz na koniec."""
        self.insert_row(len(self.data), row)

    def insert_row(self, index: int, row: list[Any]) -> None:
        """Wstawia wiersz pod wskazany indeks."""
        if self.data and len(row) != self.shape[1]:
            raise ValueError(f"Incorrect row length. Expected: {self.shape[1]}")
        self.data.insert(index, list(row))

    def add_column(self, col: list[Any]) -> None:
        """Dodaje kolumnę na koniec."""
        self.insert_column(self.shape[1], col)

    def insert_column(self, index: int, col: list[Any]) -> None:
        """Wstawia kolumnę pod wskazany indeks."""
        rows_count = self.shape[0]

        if rows_count == 0:
            self._data = [[item] for item in col]
            return

        if len(col) != rows_count:
            raise ValueError(f"Incorrect column length. Expected: {rows_count}")

        for i in range(rows_count):
            self.data[i].insert(index, col[i])

    def __repr__(self):
        return f"SimpleTable(data={self.data})"

    def __str__(self):
        return "\n".join(str(row) for row in self.data)


if __name__ == "__main__":
    obj1 = SimpleTable([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(obj1)
    obj1.add_row([10, 11, 12])
    print(obj1)
    obj1.add_column([13, 14, 15, 16])
    print(obj1)
    obj1.insert_row(1, [17, 18, 19, 21])
    print(obj1)
    print(f"Przed usunięciem: {obj1.shape}")
    del obj1.data
    print(f"Po usunięciu: {obj1.shape}")