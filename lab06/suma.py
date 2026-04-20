import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Użycie: python suma.py a b")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"Wynik: {a + b}")