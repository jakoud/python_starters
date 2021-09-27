import pandas as pd


def main():
    dane = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 3, 4, 1, 11, 2, 6, 7, 7]
    series = pd.Series(dane)
    new_series = series.drop(i for i in range(len(series)) if series[i] % 2 == 0)
    print(new_series.mean())
    print(new_series.value_counts())


main()
