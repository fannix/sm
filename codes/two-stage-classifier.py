from sklearn.datasets import load_svmlight_file
from sklearn.svm.sparse import SVC as SparseSVC
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report, confusion_matrix
import sklearn
import numpy as np


def subjective_classify(X_train, y_train, X_test, y_test):
    """Train a subjective classifier
    """

    y_train[y_train == -1] = 1
    y_test[y_test == -1] = 1

    clf = BernoulliNB()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print classification_report(y_test, y_predict)
    print confusion_matrix(y_test, y_predict)

def polarity_classify(X_train, y_train, X_test, y_test):
    """Train a positive/negative classifier
    """
    train_idx = np.where(y_train != 0)
    test_idx = np.where(y_test != 0)
    X_train = X_train[train_idx[0]]
    y_train = y_train[train_idx[0]]
    X_test = X_test[test_idx[0]]
    y_test = y_test[test_idx[0]]
    #clf = SVC(kernel='linear', C=3)
    clf = BernoulliNB()
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print classification_report(y_test, y_predict)
    print confusion_matrix(y_test, y_predict)
    

def two_stage_classify(X_train, y_train, X_test, y_test):
    """ Conduct subjective and polarity classification at the same time
    """
    y_train_sub = y_train.copy()
    y_test_sub = y_train.copy()
    y_train_sub[y_train == -1] = 1
    y_test_sub[y_test == -1] = 1

    #first stage: subjective classification
    clf = BernoulliNB()
    clf.fit(X_train, y_train_sub)
    y_predict = clf.predict(X_test)

    #second stage: polarity classification
    pol_test_idx = np.where(y_predict != 0)
    X_test_pol = X_test[pol_test_idx[0]]
    y_test_pol = y_test[pol_test_idx[0]]
    pol_train_idx = np.where(y_train != 0)
    X_train_pol = X_train[pol_train_idx[0]]
    y_train_pol = y_train[pol_train_idx[0]]
    clf.fit(X_train_pol, y_train_pol)
    pol_y_predict = clf.predict(X_test_pol)
    print classification_report(y_test_pol, pol_y_predict)
    print confusion_matrix(y_test_pol, pol_y_predict)

if __name__ == "__main__":
    train_file = "../data/2.txt"
    test_file = "../data/1.txt"
    X_train, y_train = load_svmlight_file(train_file)
    X_test, y_test = load_svmlight_file(test_file, X_train.shape[1])
    subjective_classify(X_train, y_train.copy(), X_test, y_test.copy())
    polarity_classify(X_train, y_train.copy(), X_test, y_test.copy())
    two_stage_classify(X_train, y_train.copy(), X_test, y_test.copy())

