import re

log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(ERROR)\s+(.*)$")

try:
    with open("logs.txt", "r", encoding="utf-8") as wejscie, \
            open("errors.txt", "w", encoding="utf-8") as wyjscie:

        for linia in wejscie:
            match = log_pattern.match(linia.strip())

            if match:
                data = match.group(1)
                godzina = match.group(2)
                poziom = match.group(3)
                tresc = match.group(4)

                wyjscie.write(f"{data} {godzina} -> {tresc}\n")

    print("Analiza zakończona sukcesem. Wyniki zapisano w pliku 'errors.txt'.")

except FileNotFoundError:
    print("Błąd: Plik 'logs.txt' nie istnieje.")
except IOError as e:
    print(f"Błąd operacji wejścia/wyjścia: {e}")