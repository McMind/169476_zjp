import re
log = "ERROR: file not found at /data/input.csv"
szukanie = re.findall(r"\bfile\b", log)

if __name__ == "__main__":
    print(szukanie)