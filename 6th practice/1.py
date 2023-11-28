import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.graph_objects as go
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

data = pd.read_csv("ObesityDataSet.csv")
data.Gender.replace({"Male":1, "Female":0}, inplace=True)
data.SMOKE.replace({"yes":1, "no":0}, inplace=True)
data["Height"] = data["Height"] * 100
# print(data["Height"])
data.drop(['family_history_with_overweight','FAVC', 'CAEC', 'SCC', 'CALC', 'MTRANS', 'NObeyesdad'], axis=1, inplace=True)
print(data.columns)
#2
# models = []
# score1 = []
# score2 = []
# for i in range(2, 10):
#     model = KMeans(n_clusters=i, random_state=123, init="k-means++").fit(data)
#     models.append(model)
#     score1.append(model.inertia_)
#     score2.append(silhouette_score(data, model.labels_))
#
# plt.grid()
# plt.plot(np.arange(2, 10), score1, marker = "o")
# # plt.show()

# plt.grid()
# plt.plot(np.arange(2, 10), score2, marker = "o")
# # plt.show()
# print("done")
# model1 = KMeans(n_clusters=6, random_state=123, init="k-means++")
# model1.fit(data)
# labels = model1.labels_
# data["Cluster"] = labels
# fig = go.Figure(data=[go.Scatter3d(x=data['Age'], y=data["Height"], z=data["Weight"],
#                                    mode="markers", marker_color=data["Cluster"], marker_size=4)])
# fig.show()


# 3
# model2 = AgglomerativeClustering(6, compute_distances=True)
# clustering = model2.fit(data)
# data["Cluster"] = clustering.labels_
# fig = go.Figure(data=[go.Scatter3d(x=data['Age'], y=data["Height"], z=data["Weight"],
#                                    mode="markers", marker_color=data["Cluster"], marker_size=4)])
# fig.show()

model3 = DBSCAN(eps=11, min_samples=5).fit(data)
data["Cluster"] = model3.labels_
fig = go.Figure(data=[go.Scatter3d(x=data['Age'], y=data["Height"], z=data["Weight"],
                                   mode="markers", marker_color=data["Cluster"], marker_size=4)])
fig.show()