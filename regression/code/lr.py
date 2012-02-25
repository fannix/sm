"""
Conduct linear regression y ~ bx
"""
from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import KFold

def regression(data_file):
    """
    Linear regression on data

    Parameters
    ----------
    data_file: a libsvm data file
    """
    X, y = load_svmlight_file(data_file)
    X = X.todense()
    kf = KFold(len(y), 4, indices=True)
    #lr = LinearRegression()
    lr = Lasso()
    for train, test in kf:
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        lr.fit(X_train, y_train)
        y_predict = lr.predict(X_test)
        print "mse", mean_squared_error(y_test, y_predict)
        print "r^2", lr.score(X_test, y_test)

if __name__ == "__main__":
    data_file = "../1average_label/1-2yx.txt"
    regression(data_file)
