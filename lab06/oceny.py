import sys
from array import array

def mean(a: array) -> float:
    return sum(a) / len(a)

if __name__ == '__main__':
    ilosc = len(sys.argv)
    if ilosc < 2:
        print("Podaj przynajmniej jedną ocenę")
        sys.exit(1)
    oceny = array('f', [float(ocena) for ocena in sys.argv[1:ilosc]])
    print(f"Lista ocen: {oceny.tolist()}")
    print(f"Średnia ocen: {mean(oceny):.2f}")
    print(f"Minimalna ocena: {min(oceny)}")
    print(f"Maksymalna ocena: {max(oceny)}")