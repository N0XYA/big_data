import numpy as np
import matplotlib.pyplot as plt


street = np.array([80, 98, 75, 91, 78], dtype=int)
garage = np.array([100, 82, 105, 89, 102], dtype=int)

corrcoef = np.corrcoef(street, garage)[0,1]
print(corrcoef)

plt.grid(True)
plt.title("Диаграмма рассеяния",fontsize=20)
plt.xlabel("Улица")
plt.ylabel("Гараж")
plt.scatter(street, garage)
plt.show()