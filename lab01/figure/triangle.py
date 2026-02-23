
def total_surface_area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

if __name__ == "__main__":
    a1 = 3
    a2 = 4
    a3 = 5

    print(f"Pole trojkata o bokach {a1}, {a2}, {a3} wynosi: {total_surface_area(a1, a2)}")
    print(f"Obwód trojkata o bokach {a1}, {a2}, {a3} wynosi: {perimeter(a1, a2, a3)}")
