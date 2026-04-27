import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    dataset = pd.read_csv('logs.csv')
    df = pd.DataFrame(dataset)
    wynik = df.query("level == 'ERROR'")
    print(wynik.head(5))