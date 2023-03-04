"""
@Author : Prashant Paulbudhe
@Date   : 9th Jan 2023
@Goal : Diabetes Predicator Application Using Random Forest Algorithm.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("---Application of Prashant Paulbudhe---")

print("--=Diabetes Predictor Using Decision Tree---")

diabetes = pd.read_csv('diabetes.csv')

print("Colums Of Dataset")
print(diabetes.columns)

print("First Five records of dataset")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],
diabetes['Outcome'],stratify = diabetes['Outcome'],
random_state = 66)

tree = DecisionTreeClassifier(random_state = 0)
tree.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))

print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

tree = DecisionTreeClassifier(max_depth = 3, random_state = 0)
tree.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train)))

print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

print("Feature importance:\n{}".format(tree.feature_importances_))

def plot_feature_importances_diabetes(mode):
    plt.figure(figsize = (8,9))
    n_features = 8
    plt.barh(range(n_features), mode.feature_importances_, align = 'center')
    diabetes_features = [x for i, x in enumerate(diabetes.columns) if i!=8]
    plt.yticks(np.arange(n_features),diabetes_features)
    plt.xlabel("Feature Importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)
    plt.show()

plot_feature_importances_diabetes(tree)

