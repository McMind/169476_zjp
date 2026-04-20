import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wypisywanie imienia podanego na wejściu")
    parser.add_argument("imie", type=str, help="imię")
    args = parser.parse_args()

    print(f"Witaj, {args.imie}!")