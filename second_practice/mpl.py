import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("winequality-red.csv")
columns = df.columns.values.tolist()
print(columns)
first_bar = df.loc[df["quality"] == 3]
second_bar = df.loc[df["quality"] == 8]

df = df.sort_values("citric acid")
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (10,5))
ax1.plot(df["citric acid"], df["quality"], c="crimson")
ax1.scatter(df["citric acid"].sort_values(), df["quality"], c="white", edgecolors='black', linewidth=2)
ax1.grid(linewidth=2, color='mistyrose')
ax1.set_xlabel("citric acid")
ax1.set_ylabel("quality")

df = df.sort_values("residual sugar")
ax2.plot(df["residual sugar"], df["quality"], c="crimson")
ax2.scatter(df["residual sugar"].sort_values(), df["quality"], c="white", edgecolors='black', linewidth=2)
ax2.grid(linewidth=2, color='mistyrose')
ax2.set_xlabel("residual sugar")

df = df.sort_values("pH")
ax3.plot(df["pH"], df["quality"], c="crimson")
ax3.scatter(df["pH"].sort_values(), df["quality"], c="white", edgecolors='black', linewidth=2)
ax3.grid(linewidth=2, color='mistyrose')
ax3.set_xlabel("pH")


plt.show()