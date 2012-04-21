"""
Conduct classification on SVMLight style file
"""

import numpy as np
import sklearn
import scipy as sp
from sklearn.datasets import load_svmlight_file
from sklearn.svm.sparse import LinearSVC
from sklearn import cross_validation
from sklearn.metrics import f1_score, zero_one_score


train_file = "data_svm_regression/5trainset_libsvm/train.txt"
label_file = "data_svm_regression/5trainset_libsvm/train.label"

X_train, _zero = load_svmlight_file(train_file)
X_dense = X_train.todense()
X_dense[X_dense > 1] = 1
X_train = sp.sparse.csr_matrix(X_dense)
y_train = np.loadtxt(label_file)
high = 0.5
low = -0.5
y_train[y_train >= high] = 1
y_train[y_train <= low] = -1
y_train[(y_train > low) & (y_train < high)] = 0
clf = LinearSVC(C=0.03)
scores = cross_validation.cross_val_score(clf, X_train, y_train, f1_score, cv = 5)
print scores.mean()
scores = cross_validation.cross_val_score(clf, X_train, y_train, zero_one_score, cv = 5)
print scores.mean()
