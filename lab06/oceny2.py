import argparse, sys
from array import array

def mean(a: array) -> float:
    return sum(a) / len(a)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Oceny")
    parser.add_argument("oceny", type=str, help="Oceny (po przecinku)")
    parser.add_argument("--srednia", action="store_true", help="Wypisz średnią ocen")
    parser.add_argument("--min", action="store_true", help="Wypisz minimalną ocenę")
    parser.add_argument("--max", action="store_true", help="Wypisz maksymalną ocenę")
    args = parser.parse_args()
    try:
        oceny = array('f', [float(ocena) for ocena in args.oceny.split(",")])
    except ValueError:
        print("Podaj oceny po przecinku", file=sys.stderr)
        sys.exit(1)
    print(f"Lista ocen: {oceny.tolist()}")
    if args.srednia:
        print(f"Średnia ocen: {mean(oceny):.2f}")
    if args.min:
        print(f"Minimalna ocena: {min(oceny)}")
    if args.max:
        print(f"Maksymalna ocena: {max(oceny)}")