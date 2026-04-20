import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wypisywanie kwadratu podanej liczby")
    parser.add_argument("a", type=float, help="Liczba a")
    parser.add_argument("--desc", action="store_true", help="Wypisz wynik z opisem")
    args = parser.parse_args()
    if args.desc:
        print(f"Liczę kwadrat liczby {args.a}\nWynik: {pow(args.a,2)}")
    else:
        print(pow(args.a, 2))