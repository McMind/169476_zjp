import argparse, sys

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
    parser = argparse.ArgumentParser(description="Kalkulator")
    parser.add_argument("a", type=float, help="Liczba a")
    parser.add_argument("b", type=float, help="Liczba b")
    parser.add_argument("--op", type=str, choices=['+','-','*','/'], default="+", help="Znak")
    args = parser.parse_args()
    try:
        print(f"{args.a} {args.op} {args.b} = {oblicz(args.a, args.b, args.op)}")
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)