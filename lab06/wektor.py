import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wypisywanie wektora między podanymi punktami")
    parser.add_argument("x1", type=int, help="x1")
    parser.add_argument("y1", type=int, help="y1")
    parser.add_argument("x2", type=int, help="x2")
    parser.add_argument("y2", type=int, help="y2")
    args = parser.parse_args()
    print(f"Wektor: [{args.x2 - args.x1}, {args.y2 - args.y1}]")