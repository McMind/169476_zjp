import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Program do analizy ocen akademickich."
    )

    parser.add_argument(
        'oceny',
        type=float,
        nargs='*',
        help='Lista ocen oddzielonych spacjami (zakres 2-5)'
    )

    parser.add_argument('--srednia', action='store_true', help='Oblicza i wypisuje średnią ocen')
    parser.add_argument('--min', action='store_true', help='Wypisuje najniższą ocenę')
    parser.add_argument('--max', action='store_true', help='Wypisuje najwyższą ocenę')
    parser.add_argument('--lista', action='store_true', help='Wypisuje listę podanych ocen')

    args = parser.parse_args()

    if not args.oceny:
        print("Błąd: Nie podano żadnych ocen.", file=sys.stderr)
        sys.exit(1)

    for ocena in args.oceny:
        if ocena < 2.0 or ocena > 5.0:
            print(f"Błąd: Ocena {ocena} jest spoza dozwolonego zakresu (2 do 5).", file=sys.stderr)
            sys.exit(1)

    if args.lista:
        formatowane_oceny = [int(o) if o.is_integer() else o for o in args.oceny]
        print(f"Podane oceny: {formatowane_oceny}")

    if args.srednia:
        srednia = sum(args.oceny) / len(args.oceny)
        print(f"Średnia ocen: {srednia:.2f}")

    if args.min:
        najnizsza = min(args.oceny)
        print(f"Najniższa ocena: {str(int(najnizsza)) if najnizsza.is_integer() else str(najnizsza)}")

    if args.max:
        najwyzsza = max(args.oceny)
        print(f"Najwyższa ocena: {str(int(najwyzsza)) if najwyzsza.is_integer() else str(najwyzsza)}")

    if not (args.srednia or args.min or args.max or args.lista):
        print("Podano oceny poprawnie, ale nie wybrano żadnej flagi (--srednia, --min, --max, --lista).")


if __name__ == '__main__':
    main()