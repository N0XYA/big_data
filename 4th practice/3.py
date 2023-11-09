import pandas as pd

df = pd.read_csv("insurance.csv")

# print(df.info())
uniques = df.region.unique()
print(uniques)