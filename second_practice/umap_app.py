import pandas as pd
import umap
import numpy as np
from time import time
import matplotlib.pyplot as plt


start_time = time()
digits = pd.read_csv("fashion-mnist_train.csv")

embedding = umap.UMAP(n_neighbors=10,
                      min_dist=0.01,
                      metric='correlation').fit_transform(digits.iloc[:20000, 1:])


plt.figure(figsize=(12,12))
plt.scatter(embedding[:20000, 0], embedding[:20000, 1],
            c=digits.iloc[:20000, 0],
            edgecolor='none',
            alpha=0.80,
            s=10)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.title('Fashion MNIST UMAP', fontsize=24)
# plt.axis('off')
end_time = time()
exec_time = end_time - start_time
print("Time: ", exec_time)
plt.show()