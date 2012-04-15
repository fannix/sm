import numpy as np
import sklearn
from sklearn.datasets import load_svmlight_file
from sklearn.svm.sparse import SVR
from sklearn import cross_validation
from sklearn.metrics import f1_score, zero_one_score
import sys
import pickle

def SVR_train(X_train, y_train, output_model):
    """ Train using Support Vector Regression
    """

    svr = SVR(C = 0.03, kernel = "linear", epsilon = 0.2)
    svr.fit(X_train, y_train)
    pickle.dump(svr, open(output_model, 'w'))


def SVR_predict(X_predict, model):
    """Predict using Support Vector Regression
    """
    svr = pickle.load(open(model))
    return svr.predict(X_predict)

def main():
    action = sys.argv[1]
    if action == "train":
        X_train, _ = load_svmlight_file(sys.argv[2])
        y_train = np.loadtxt(sys.argv[3])
        model = sys.argv[4]
        SVR_train(X_train, y_train, model)
    elif action == "predict":
        X_predict, _ = load_svmlight_file(sys.argv[2])
        model = sys.argv[3]
        y_predict = SVR_predict(X_predict, model)
        for y in y_predict:
            print y
    elif action == "cross-validation":
        X_train = sys.argv[2]
        y_train = sys.argv[3]
    else:
        print "usage: train predict or cross-validation"
        sys.exit(-1)

if __name__ == "__main__":
    main()
