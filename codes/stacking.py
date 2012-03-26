"""
Conduct classification on SVMLight style file
"""

import sklearn
import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn.datasets import load_svmlight_file
from sklearn import cross_validation
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import f1_score, zero_one_score
from collections import defaultdict


def get1v1dataset(X, y, label1, label2):
    """
    Obtain dataset belong to label1 and label2 to create a 1v1 classifier
    """
    X1 = X[y == label1]
    X2 = X[y == label2]
    y1 = y[y == label1]
    y2 = y[y == label2]

    X = np.vstack((X1, X2))
    y = np.hstack((y1, y2))
    return X, y

def classify():
    """
    cross validate a model and test

    train_file: file that the model is trained on
    """
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    clf1v2 = svm.SVC(C = 0.1)
    clf1v3 = svm.SVC(C = 0.1)
    clf2v3 = svm.SVC(C = 0.1)
    skf = StratifiedKFold(y, 2)

    di = defaultdict(lambda: 0)

    for train, test in skf:
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        X1v2, y1v2 = get1v1dataset(X_train, y_train, 0, 1)
        X1v3, y1v3 = get1v1dataset(X_train, y_train, 0, 2)
        X2v3, y2v3 = get1v1dataset(X_train, y_train, 1, 2)

        clf1v2.fit(X1v2, y1v2)
        clf1v3.fit(X1v3, y1v3)
        clf2v3.fit(X2v3, y2v3)

        predict1v2 = clf1v2.predict(X_test)
        predict1v3 = clf1v3.predict(X_test)
        predict2v3 = clf2v3.predict(X_test)
        for i in range(len(y_test)):
            s = "%d%d%d%d" % (predict1v2[i], predict1v3[i],
                    predict2v3[i], y_test[i])
            di[s] += 1

    print di

if __name__ == "__main__":
    classify()
