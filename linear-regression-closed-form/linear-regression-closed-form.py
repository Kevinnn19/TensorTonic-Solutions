import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    trans = X.T
    pro1 = trans @ X
    pro2 = trans @ y
    inverse = np.linalg.inv(pro1)
    return inverse @ pro2