import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objs as go


df = pd.read_csv("insurance.csv")
df = df.drop("sex", axis=1)
df = df.drop("smoker", axis=1)
df = df.drop("region", axis=1)
columns = df.columns.values.tolist()
fig, ax = plt.subplots(1, len(columns), figsize=(12,4))
for column in columns:
    ind = columns.index(column)
    if ind == 2:
        ax[ind].hist(df[column].values, edgecolor='black', bins=6)
        ax[ind].set_xlabel(column)
        continue
    ax[ind].hist(df[column], edgecolor='black')
    ax[ind].set_xlabel(column)
    print(column, ind)
plt.show()


# print(df.describe())
# print(df.head())