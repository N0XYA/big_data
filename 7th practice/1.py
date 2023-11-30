import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
import catboost as cb
from time import time
# 1
data = load_wine(as_frame=True)
predicts = data.data
target = data.target

# print(predicts.info())
# 2
A_train, A_test, y_train, y_test = train_test_split(predicts, target, train_size=0.8)
random_forest = RandomForestClassifier()
params_grid = {
	"max_depth": [12, 18],
	"min_samples_leaf": [3, 10],
	"min_samples_split": [6, 12],
}
grid_search_random_forest = GridSearchCV(estimator=random_forest, param_grid=params_grid, scoring="f1_macro", cv=4)

start_time = time()
grid_search_random_forest.fit(A_train, y_train)
time1 = time() - start_time

best_model = grid_search_random_forest.best_estimator_
y_preds_d = best_model.predict(A_train)
print('F1 мера для тренировочных данных', f1_score(y_preds_d, y_train, average='macro'))
y_pred = best_model.predict(A_test)
score1 = f1_score(y_pred, y_test, average='macro')
print('F1 мера для тестовых данных', score1)

# 3
model_catboost_clf = cb.CatBoostClassifier(iterations=1000, task_type="GPU", devices='0')

start_time = time()
model_catboost_clf.fit(A_train, y_train)
time2 = time() - start_time

y_preds_t = model_catboost_clf.predict(A_train, task_type="CPU")
print('F1 мера для тренировочных данных', f1_score(y_preds_t, y_train, average='macro'))
y_pred = model_catboost_clf.predict(A_test, task_type="CPU")
score2 = f1_score(y_pred, y_test, average='macro')
print('F1 мера для тестовых данных', score2)

# 4

print(f'Баггинг - Время: {time1}, Качество: {score1}')
print(f'Бустинг - Время: {time2}, Качесвто: {score2}')