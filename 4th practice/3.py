import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd


df = pd.read_csv("insurance.csv")
print(df.info())
uniques = df.region.unique()
print(uniques)

frame = pd.DataFrame({"regions": df.region.values, "bmi": df.bmi.values})
groups = frame.groupby("regions").groups
southwest = (df["bmi"].loc[df["region"] == uniques[0]])
southeast = df["bmi"].loc[df["region"] == uniques[1]]
northwest = df["bmi"].loc[df["region"] == uniques[2]]
northeast = df["bmi"].loc[df["region"] == uniques[3]]

f_oneway = stats.f_oneway(southwest, southeast, northwest, northeast)
print(f_oneway)
print("===")
model = ols("bmi ~ regions", data= frame).fit()
anova_result = sm.stats.anova_lm(model, typ= 2)
print(anova_result)
print("===")
reg_pairs = []
for reg1 in range(3):
    for reg2 in range(reg1 + 1, 4):
        reg_pairs.append((uniques[reg1], uniques[reg2]))

count = 0
for reg1, reg2 in reg_pairs:
    count += 1
    print(reg1, reg2)
    print(stats.ttest_ind(frame.bmi[groups[reg1]], frame.bmi[groups[reg2]]))

alpha = 0.05 / count

print(f"alpha is {alpha}")
print("===")

tukey = pairwise_tukeyhsd(endog=df.bmi, groups=df.region, alpha=0.05)
tukey.plot_simultaneous()
plt.vlines(x=31, ymin=-10, ymax=10, color='red')
print(tukey.summary())
plt.show()

frame = pd.DataFrame({'region': df.region, 'bmi': df.bmi, 'sex': df.sex})
model = ols('bmi ~ C(region) + C(sex) + C(region):C(sex)', data=frame).fit()
anova = sm.stats.anova_lm(model, typ=2)
print(anova)

df['combination'] = df.region + ' / ' + df.sex

tukey = pairwise_tukeyhsd(endog=df['bmi'], groups=df['combination'], alpha=0.05)
tukey.plot_simultaneous()
plt.vlines(x=31, ymin=-10, ymax=10, color='red')
print(tukey.summary())
plt.show()