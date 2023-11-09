import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as sts
import plotly.graph_objs as go
import random


df = pd.read_csv("./insurance.csv")
df = df.drop("sex", axis=1)
df = df.drop("smoker", axis=1)
df = df.drop("region", axis=1)
columns = df.columns.values.tolist()
def bars():
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
    return


def box():
    fig, ax = plt.subplots(1, len(columns), figsize=(12, 4))
    for col in columns:
        ind =columns.index(col)
        print(ind)
        ax[ind].boxplot(df[col], vert=False)
        ax[ind].set_title(col)
        ax[ind].grid()
    plt.show()


def theorem():
    n = 300
    len_samples = [10, 50, 100]
    fig, ax = plt.subplots(len(len_samples), figsize=(30, 8))
    means = []
    dist95 = {}
    dist99 = {}
    for i in range(len(len_samples)):
        sample_means = []
        for k in range(n):
            sample = np.random.choice(df["charges"], size=len_samples[i], replace=True)
            sample_means.append(np.mean(sample))
        means.append(sample_means)
        ax[i].hist(sample_means, bins=15, edgecolor="black", color= "green")
        ax[i].set_title("sample len = " + str(len_samples[i]))
        sample_means = np.array(sample_means)
        print("Длина выборки", len_samples[i])
        print("Std ", sample_means.std())
        print("Mean ", np.mean(sample_means))
        dist95[len_samples[i]] = [
            np.mean(sample_means) - 1.96 * sample_means.std() / np.sqrt(len_samples[i]),
            np.mean(sample_means) + 1.96 * sample_means.std() / np.sqrt(len_samples[i])
        ]
        dist99[len_samples[i]] = [
            np.mean(sample_means) - 2.58 * sample_means.std() / np.sqrt(len_samples[i]),
            np.mean(sample_means) + 2.58 * sample_means.std() / np.sqrt(len_samples[i])
        ]
    print("Доверительный интервал 95% ", dist99)
    print("Доверительный интервал 99%", dist99)
    plt.show()

def normal_distribution():
    normal_quantiles = np.random.normal(0, 1, 1338)
    x = np.sort(normal_quantiles)
    y_bmi = np.sort(df['bmi'])
    y_charges = np.sort(df['charges'])
    sns.jointplot(x=x, y=y_bmi, kind="reg", truncate=True, color="blue")
    sns.jointplot(x=x, y=y_charges, kind="reg", truncate=True, color="purple")
    test_bmi = (df['bmi'] - np.mean(df['bmi'])) / df['bmi'].std()
    test_charges = (df['charges'] - np.mean(df['charges'])) / df['charges'].std()
    print("KS-тест для bmi: ", sts.kstest(test_bmi, 'norm'))
    print("KS-тест для charges: ", sts.kstest(test_charges, 'norm'))
    plt.show()


normal_distribution()