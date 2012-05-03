import numpy as np
import sklearn
from sklearn.datasets import load_svmlight_file
from sklearn.svm.sparse import SVR
from sklearn.linear_model.sparse import Lasso
from sklearn.linear_model.sparse import ElasticNet
from sklearn import cross_validation
from sklearn.metrics import f1_score, zero_one_score, r2_score
from sklearn.metrics import mean_square_error
import sys


X_train, _ = load_svmlight_file("data_svm_regression/5trainset_libsvm/train.txt")
y_train = np.loadtxt("data_svm_regression/5trainset_libsvm/train.label")

#rm = SVR(C = 0.1, kernel = "linear", epsilon = 0.3)
#rm = Lasso(alpha = 0.001)
rm = ElasticNet(alpha = 0.001, rho=0.7)

y_predict = np.zeros(X_train.shape[0])
kf = cross_validation.KFold(X_train.shape[0], k = 5)
for train_index, test_index in kf:
    rm.fit(X_train[train_index], y_train[train_index])
    y_predict[test_index] = rm.predict(X_train[test_index])


print >> sys.stderr, mean_square_error(y_train, y_predict)
print >> sys.stderr, r2_score(y_train, y_predict)

#for y in y_predict:
    #print y

