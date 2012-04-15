"""
Conduct classification on SVMLight style file
"""

from sklearn.datasets import load_svmlight_file
from sklearn import grid_search
from sklearn.svm import SVC
from sklearn.svm.sparse import SVC as SparseSVC
from sklearn.svm.sparse import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from pprint import pprint
import sklearn


def classify(train_file, test_file):
    """
    Train a model and test

    train_file: file that the model is trained on
    test_file: file that is used to test the model
    """
    X_train, y_train = load_svmlight_file(train_file)
    X_test, y_test = load_svmlight_file(test_file, X_train.shape[1])
    #X_train = X_train.todense()
    #X_test = X_test.todense()
    clf = LinearSVC(C=0.1)
    #clf = SparseSVC(kernel='linear', C=100)
    #clf = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    print sklearn.metrics.classification_report(y_test, y_predict)
    print sklearn.metrics.confusion_matrix(y_test, y_predict)
    #print clf.coef_

    #grid search
    parameters = {'C': [0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]}
    grid_clf = grid_search.GridSearchCV(clf, parameters, score_func = f1_score, verbose=10)
    grid_clf.fit(X_train, y_train)
    print grid_clf.best_estimator
    pprint(grid_clf.grid_scores_)

    #learning curve
    #m, n = X_train.shape
    #step = m/10
    #for i in range(step, m, step):
        #clf.fit(X_train[:i], y_train[:i])
        #y_predict = clf.predict(X_test)
        #print sklearn.metrics.classification_report(y_test, y_predict)
        #print sklearn.metrics.confusion_matrix(y_test, y_predict)



if __name__ == "__main__":
    train_file = "../data/2.txt"
    test_file = "../data/1.txt"
    classify(train_file, test_file)
