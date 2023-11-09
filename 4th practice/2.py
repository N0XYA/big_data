import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import os
import matplotlib.pyplot as plt

df = pd.read_csv("../second_practice/winequality-red.csv")
# print(df.info())
# print(df.isnull().sum())

corr_matrix = df.corr().quality.to_frame().round(2)
corr_matrix.style.background_gradient(cmap='coolwarm')
# print(corr_matrix)
y = df["quality"].values
x = df["alcohol"].values

X = df[["alcohol"]]
# y = df["quality"]
# x = np.array(X, type(float))
# y = np.array(y, type(float))

def mserror(x, w1, w0, y):
    y_pred = w1 * x + w0
    return np.sum((y - y_pred)**2) / len(y_pred)


def gr_mserror(x, w1, w0, y):
    y_pred = w1 * x + w0
    return np.array([2 / len(x) * np.sum((y-y_pred)) * -1, 2 / len(x) *
                     np.sum((y - y_pred) * -x)])


eps = 0.000001
w1 = 0
w0 = 0
learning_rate = 0.001
next_w1 = w1
next_w0 = w0
n = 1000000
for i in range(n):
    cur_w1 = next_w1
    cur_w0 = next_w0

    next_w0 = cur_w0 - learning_rate * gr_mserror(x, cur_w1, cur_w0, y)[0]
    next_w1 = cur_w1 - learning_rate * gr_mserror(x, cur_w1, cur_w0, y)[1]

    # print(f"iter {i}")
    # print(f"curr point {cur_w1, cur_w0}")

    if (abs(cur_w1 - next_w1) <= eps) and (abs(cur_w0 - next_w0) <= eps):
        break

model = LinearRegression()

model.fit(X, y)

# print(model.coef_, model.intercept_)

fig = plt.figure(figsize=(10, 6))


our_y = next_w1 * X + next_w0

print(f"наклон: {next_w0}, сдвиг: {next_w1}")
print(f"mse: {mserror(x, next_w1, next_w0, y)}")
x = np.arange(0, 40)
model_a = model.coef_[0]
model_b = model.intercept_
sklearn_y = model_a * X + model_b
# plt.plot(X, sklearn_y, color="r")
plt.plot(X, our_y, "--g")
plt.scatter(X, y, alpha=0.7)
plt.show()
