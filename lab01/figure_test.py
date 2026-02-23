if __name__ == "__main__":
    from figure import rectangle, triangle

    a1 = 5
    a2 = 12
    a3 = 13

    print(f"Pole trojkata o bokach {a1}, {a2}, {a3} wynosi: {triangle.total_surface_area(a1, a2)}")
    print(f"Obwód trojkata o bokach {a1}, {a2}, {a3} wynosi: {triangle.perimeter(a1, a2, a3)}")

    print(f"Pole prostokąta o bokach {a1}, {a2} wynosi: {rectangle.total_surface_area(a1, a2)}")
    print(f"Obwód prostokąta o bokach {a1}, {a2} wynosi: {rectangle.perimeter(a1, a2)}")