"""
Conduct linear regression y ~ bx
"""
from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LinearRegression
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
    kf = KFold(len(y), 2, indices=False)
    print X.shape, y.shape
    for train, test in kf:
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        print X_train.shape, y_train.shape
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        y_predict = lr.predict(X_test)
        print mean_squared_error(y_test, y_predict)

if __name__ == "__main__":
    data_file = "../1average_label/1-2yx.txt"
    regression(data_file)
