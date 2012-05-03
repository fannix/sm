import numpy as np
import sklearn
from sklearn.datasets import load_svmlight_file
from sklearn.svm.sparse import SVR
from sklearn import cross_validation
from sklearn.metrics import f1_score, zero_one_score, r2_score
from sklearn.metrics import mean_square_error
from sklearn.linear_model.sparse import ElasticNet
from sklearn.linear_model.sparse import Lasso
import sys
import pickle

def regression_train(X_train, y_train, output_model):
    """ Train using Lasso
    """

    svr =  Lasso(alpha = 0.001)
    svr.fit(X_train, y_train)
    pickle.dump(svr, open(output_model, 'w'))


def regression_predict(X_predict, model):
    """Predict using Lasso
    """
    svr = pickle.load(open(model))
    return svr.predict(X_predict)

def main():
    action = sys.argv[1]
    if action == "train":
        X_train, _ = load_svmlight_file(sys.argv[2])
        y_train = np.loadtxt(sys.argv[3])
        model = sys.argv[4]
        regression_train(X_train, y_train, model)
    elif action == "predict":
        vocab = sys.argv[2]
        n_features = len(open(vocab).readlines())
        X_predict, _ = load_svmlight_file(sys.argv[3], n_features=n_features)
        model = sys.argv[4]
        y_predict = regression_predict(X_predict, model)
        for y in y_predict:
            print y
    else:
        print "usage: train/predict"
        sys.exit(-1)

if __name__ == "__main__":
    main()
