import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


df = pd.read_csv("insurance.csv")
bmi = df["bmi"].values
charges = df["charges"].values
bmi_mean = np.mean(bmi)
charges_mean = np.mean(charges)
bmi_moda = sts.mode(bmi)
charges_moda = sts.mode(charges)
bmi_med = np.median(bmi)
charges_med = np.median(charges)

print("bmi")
print("Среднее:", bmi_mean)
print("Мода:", bmi_moda)
print("Медиана:", bmi_med)
print("===========")
print("charges")
print("Среднее:", charges_mean)
print("Мода:", charges_moda)
print("Медиана:", charges_med)

def histogramms():
    fig, ax = plt.subplots(1, 2, figsize=(12,4))
    ax[0].hist(bmi, edgecolor='black', color="gray")
    ax[0].axvline(x=bmi_mean, color="red")
    ax[0].axvline(x=bmi_moda[0], color="green")
    ax[0].axvline(x=bmi_med, color="blue")
    ax[1].hist(charges, edgecolor="black", color="grey")
    ax[1].axvline(x=charges_mean, color="red")
    ax[1].axvline(x=charges_moda[0], color="green")
    ax[1].axvline(x=charges_med, color="blue")
    fig.legend(["Среднее", "Мода", "Медиана"])
    plt.show()


def box_plots():
    pass