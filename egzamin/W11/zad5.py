from functools import partial


def apply_tax(netto, vat):
    return (1 + vat / 100) * netto


vat_23 = partial(apply_tax, vat=23)

vat_8 = partial(apply_tax, vat=8)

if __name__ == "__main__":
    print(f"Wynik doliczenia podatku 23% do 200 => {vat_23(200)}")
    print(f"Wynik doliczenia podatku 8% do 50 => {vat_8(50)}")
