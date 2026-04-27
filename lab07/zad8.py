import pandas as pd

if __name__ == '__main__':
    dataset = pd.read_csv('zdania.csv')
    df = pd.DataFrame(dataset)
    df['liczba_slow'] = df['zdanie'].str.count(' ') + 1
    wedlug_ilosci_slow = sorted(zip(df['zdanie'], df['liczba_slow']), key=lambda x: x[1])
    print(wedlug_ilosci_slow)