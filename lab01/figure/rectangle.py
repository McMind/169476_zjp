
def total_surface_area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

if __name__ == "__main__":
    a1 = 6
    a2 = 8

    print(f"Pole prostokąta o bokach {a1}, {a2} wynosi: {total_surface_area(a1, a2)}")
    print(f"Obwód prostokąta o bokach {a1}, {a2} wynosi: {perimeter(a1, a2)}")