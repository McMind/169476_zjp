from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, title: str, ratings: list[float | int]):
        self.title = title
        self.ratings = ratings

    @property
    def average_rating(self) -> float:
        if self.ratings is None:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.ratings == other.ratings

    def __lt__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.average_rating < other.average_rating

    def __repr__(self):
        return f"Book({self.title}, {self.average_rating:.2f})"


obj1 = Book("Harry Potter", [3, 4, 3])
obj2 = Book("Harry Potter 2", [3, 5, 4])
obj3 = Book("Wiedźmin", [4, 5, 2])
print(obj1)
print(obj2)
print(obj3)

print(obj1 == obj2)

print(obj1 < obj2)

print(obj1 > obj2)

print(obj1 >= obj3)

print(obj1 <= obj3)

list1 = [obj1, obj2, obj3]

sorted_list1 = sorted(list1, reverse=True)

print(sorted_list1)
