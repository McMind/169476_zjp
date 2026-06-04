from functools import total_ordering


@total_ordering
class Player:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    @property
    def average_score(self):
        if self.scores is None:
            return 0
        return sum(self.scores) / len(self.scores)

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.average_score == other.average_score

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.average_score < other.average_score

    def __repr__(self):
        return f"Player({self.name}, {self.average_score})"


if __name__ == "__main__":
    obj1 = Player("Jan", [1, 2, 3, 4])
    obj2 = Player("Adam", [3, 0, 1, 1])
    obj3 = Player("Grzegorz", [5, 3, 2, 8])

    print("Porównania")
    print(f"{obj1} < {obj2} => {obj1 < obj2}")
    print(f"{obj1} <= {obj2} => {obj1 <= obj2}")
    print(f"{obj1} > {obj2} => {obj1 > obj2}")
    print(f"{obj2} == {obj3} => {obj2 == obj3}")

    print("Sortowanie malejąco po średniej liczbie punktów")
    list1 = [obj1, obj2, obj3]
    print("Przed sortowaniem")
    print(list1)
    list2 = sorted(list1, reverse=True)
    print("Po sortowaniu")
    print(list2)
