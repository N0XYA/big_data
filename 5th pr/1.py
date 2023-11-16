import numpy as np
import sklearn
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import plotly.graph_objs as go
import plotly.express as px


data = load_wine(as_frame=True)
predictords = data.data
target = data.target
target_names = data.target_names
fig = go.Figure(data=[go.Bar(x = target_names, y = [len(target.loc[target == 0]), len(target.loc[target == 1]),
                                                    len(target.loc[target == 2])])])
fig.update_layout(title="Data showcase")
fig.show()

x_train, x_test, y_train, y_test = train_test_split(predictords, target, train_size=0.8,
                                                    shuffle=True, random_state=271)

print("x train", x_train.shape, "x test", x_test.shape, "y train", y_train.shape, "y test", y_test.shape)
# REGRESSION
model = LogisticRegression(random_state=271)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print("Predictions:\n", y_predict)
print("Expected:\n", np.array(y_test))
print(classification_report(y_test, y_predict))
fig = px.imshow(confusion_matrix(y_test, y_predict), text_auto=True)
fig.update_layout(title="Regression", xaxis_title = "Target", yaxis_title = "Prediction")
fig.show()

# SVM
param_kernel = ("linear", "rbf", "poly", "sigmoid")
parameters = {"kernel": param_kernel}
model = SVC()
grid_search_svm = GridSearchCV(estimator=model, param_grid=parameters, cv=6)
grid_search_svm.fit(x_train, y_train)
best_model = grid_search_svm.best_estimator_
print("best model: ", best_model.kernel)
svm_preds = best_model.predict(x_test)
print("Predictions:\n", svm_preds)
print("Expected:\n", np.array(y_test))
print(classification_report(y_test, svm_preds))
fig = px.imshow(confusion_matrix(y_test, svm_preds), text_auto=True)
fig.update_layout(title="SVM", xaxis_title = "Target", yaxis_title = "Prediction")
fig.show()

# KNN
number_of_neighbours = np.arange(3, 10)
model_KNN = KNeighborsClassifier()
params = {"n_neighbors": number_of_neighbours}
grid_search = GridSearchCV(estimator=model_KNN, param_grid=params, cv = 6)
grid_search.fit(x_train, y_train)
print("best score: ", grid_search.best_score_)
print("best num of k:", grid_search.best_estimator_)
knn_preds = grid_search.predict(x_test)
print("Predictions:\n", knn_preds)
print("Expected:\n", np.array(y_test))
print(classification_report(y_test, knn_preds))
fig = px.imshow(confusion_matrix(y_test, knn_preds), text_auto=True)
fig.update_layout(title="KNN", xaxis_title = "Target", yaxis_title = "Prediction")
fig.show()
