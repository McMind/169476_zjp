import sys

def oblicz(a1: float, b1: float, sign: str) -> float:
    match sign:
        case '+':
            return a1 + b1
        case '-':
            return a1 - b1
        case '*':
            return a1 * b1
        case '/':
            return a1 / b1
    raise TypeError("Nieprawidłowy znak")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Użycie: python kalkulator.py a 'znak' b", file=sys.stderr)
        sys.exit(1)
    try:
        a = float(sys.argv[1])
        znak = str(sys.argv[2])
        b = float(sys.argv[3])
        lista_znakow = ['+', '-', '*', '/']
        if znak not in lista_znakow:
            print(f"Wybierz znak z: {lista_znakow}", file=sys.stderr)
            sys.exit(1)
        print(f"{a} {znak} {b} = {oblicz(a, b, znak)}")
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)