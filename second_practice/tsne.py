import pandas as pd
import numpy as np
from time import time


from  matplotlib import offsetbox
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import seaborn as sns
import plotly.graph_objects as go

sns.set(style="white", context="notebook",rc={'figure.figsize':(14,10)})

from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import warnings
warnings.filterwarnings("ignore")

train = pd.read_csv("fashion-mnist_train.csv")

y = train.loc[:, "label"].values
x = train.loc[:,"pixel1":].values

print(x.shape)
print(y)

def plot_digits(data):
    fig, axes = plt.subplots(4, 10, figsize=(10, 4),
                             subplot_kw={'xticks':[], 'yticks':[]},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(28, 28),
                  cmap='binary', interpolation='nearest',
                  clim=(0, 16))
    plt.show()

standardized_data = StandardScaler().fit_transform(x)
print(standardized_data.shape)

x_subset = x[0:10000]
y_subset = y[0:10000]

print(np.unique(y_subset))
tsne = TSNE(random_state = 42, n_components=2,verbose=0, perplexity=70, n_iter=300).fit_transform(x_subset)

plt.scatter(tsne[:, 0], tsne[:, 1], s= 5, c=y_subset, cmap='Spectral')
plt.gca().set_aspect('equal', 'datalim')
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.title('Fashion MNIST t-SNE', fontsize=24)
plt.show()