import re
text = "Cena: 49.99 PLN, rabat: 10.50 PLN"
liczby = re.findall(r"\d+\.\d+", text)

if __name__ == "__main__":
    print(liczby)