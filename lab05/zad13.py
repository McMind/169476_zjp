import re
all_files = ["notes.txt", "data.csv", "image.png", "report.xlsx", "archive.parquet"]
rozszerzenia = ["csv", "xlsx", "parquet"]
pattern = rf"\.({'|'.join(rozszerzenia)})$"
data_files = [f for f in all_files if re.search(pattern, f)]

if __name__ == '__main__':
    print(data_files)