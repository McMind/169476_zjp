import re
record = "  Jan Kowalski  (ur. 1990) "
wynik = re.sub(r'\(.*?\)', '', record)

if __name__ == '__main__':
    print(f"'{wynik}'")