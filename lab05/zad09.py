import re
text = "Raport_2024 raport_2025 RAPORT_2026"
liczby_4 = re.findall(r"\d{4}", text)

if __name__ == '__main__':
    print(liczby_4)