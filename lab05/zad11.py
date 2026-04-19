import re
files = ["data.csv", "report.pdf", "sales.xlsx", "model.pkl"]
wynik = [f for f in files if re.search(r'(csv|xlsx)$', f)]

if __name__ == '__main__':
    print(wynik)