"""
Conduct classification on SVMLight style file
"""

import sklearn
from sklearn.datasets import load_svmlight_file
from sklearn.svm.sparse import LinearSVC
from sklearn import cross_validation
from sklearn.metrics import f1_score, zero_one_score



def classify(train_file):
    """
    cross validate a model and test

    train_file: file that the model is trained on
    """
    X_train, y_train = load_svmlight_file(train_file)
    clf = LinearSVC(C=0.1)
    scores = cross_validation.cross_val_score(clf, X_train, y_train, f1_score)
    print scores.mean()
    scores = cross_validation.cross_val_score(clf, X_train, y_train, zero_one_score)
    print scores.mean()

if __name__ == "__main__":
    train_file = "../data/2.txt"
    classify(train_file)
