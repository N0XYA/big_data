import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from apriori_python import apriori as a1
from apyori import apriori as a2
from efficient_apriori import apriori
from fpgrowth_py import fpgrowth
import time

data = pd.read_csv("data.csv")
# 1
# print(data.info())

# 2
# print(data.stack().value_counts())
# print(data.stack().value_counts(normalize=True))
# data.stack().value_counts(normalize=True)[0:20].plot(kind="bar")
# plt.title("Относительная частота встречаемости")
# data.stack().value_counts().apply(lambda item: item / data.shape[0])[0:20].plot(kind="bar")
# plt.title("Фактическая частота встречаемости")
# plt.xticks(rotation=45)
# plt.show()

# 3
transactions = []
for i in range(data.shape[0]):
    row = data.iloc[i].dropna().tolist()
    transactions.append(row)

t = []
# 3.1
start = time.perf_counter()
t1, rules = a1(transactions, minSup=0.012, minConf= 0.4) # s=0.012, c=0.4
time1 = time.perf_counter()-start
t.append(time1)
# for rule in rules:
#     print(rule)

# 3.2
start = time.perf_counter()
rules = a2(transactions=transactions,
                min_support=0.012,
                min_confidence=0.4,
                min_lift=1.0001)
results = list(rules)
time2 = time.perf_counter() - start
t.append(time2)
# for r in results:
#     for subset in r[2]:
#         print(subset[0], subset[1])
#         print("Support: {0}; Confidence: {1},; Lift: {2}".format(r[1], subset[2], subset[3]))
#         print()

# 3.3
start = time.perf_counter()
itemsets, rules = apriori(transactions, min_support=0.012, min_confidence=0.4)
time3 = time.perf_counter() - start
t.append(time3)

# for i in range(len(rules)):
#     print(rules[i])

# 4
start = time.perf_counter()
itemsets, rules = fpgrowth(transactions, minSupRatio=0.012, minConf=0.4)
time4 = time.perf_counter() - start
t.append(time4)
#
# for i in range(len(rules)):
#     print(rules[i])

# 5
print("Apriori", t[0], "\n")
print("Apriori 2", t[1], "\n")
print("Efficient apriori", t[2], "\n")
print("fpgrowth", t[3], "\n")
plt.bar(["Apriori", "Apriori 2", "Efficient apriori", "fpgrowth"], t)
plt.title("Время работы алгоритмов")
plt.show()