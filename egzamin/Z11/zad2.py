from functools import total_ordering


@total_ordering
class Student:

    def __init__(self, name: str, grades: list[float | int]):
        self.name = name
        self.grades = grades

    @property
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average == other.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average < other.average

    def __repr__(self):
        return f"Student({self.name}, {self.average:.2f})"


s1 = Student("Jan Kowalski", [4, 5, 4, 3])
s2 = Student("Anna Nowak", [5, 5, 5, 4])
s3 = Student("Piotr Wiśniewski", [3, 4, 4, 5])

students_list = [s1, s2, s3]

print("Porównania studentów:")
print(f"{s1} <  {s2} : {s1 < s2}")
print(f"{s1} <= {s3} : {s1 <= s3}")
print(f"{s2} >  {s1} : {s2 > s1}")
print(f"{s1} == {s3} : {s1 == s3}")

print("\nSortowanie listy studentów malejąco:")
sorted_students = sorted(students_list, reverse=True)
print(sorted_students)