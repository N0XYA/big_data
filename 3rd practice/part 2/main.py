import pandas as pd
import numpy as np
import scipy.stats as sts


def missing_val(df):
    for column in df.columns:
        missing = np.mean(df[column].isna() * 100)
        print(f" {column} : {round(missing, 1)}%")
    print("==============================================")
    return


def find_duplicates(df):
    a = sum(df.duplicated())
    print("Дубликатов: ", a)
    df.drop_duplicates()
    return


def deaths(df):
    a = 0
    for i in df.values:
        if i[5] > 3000:
            a += 1
            print(f"Страна: {i[6]}, дата: {i[0]}, кол-во смертей: {i[5]}")
    print("Количество дней ", a)
    return


def main():
    df = pd.read_csv("ECDCCases.csv")
    # missing_val(df)
    df.drop(columns=["geoId", 'Cumulative_number_for_14_days_of_COVID-19_cases_per_100000'], inplace=True)
    median = np.mean(df['popData2019'])
    df['popData2019'].fillna(median, inplace=True)
    df['countryterritoryCode'].fillna("other", inplace=True)
    # missing_val(df)
    # print(df.info())
    # deaths(df)
    find_duplicates(df)
    return


if __name__ == "__main__":
    main()