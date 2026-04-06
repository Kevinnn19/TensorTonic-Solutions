import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    try:
        X = np.asarray(X, dtype=float)
    except:
        return None
    N = X.shape[0]
    if X.ndim != 2 :
        return None
    if N < 2 :
        return None
    if X.size == 0 :
        return None
    mu = np.mean(X, axis = 0)
    Xcen = X - mu
    sample = 1 / (N - 1)
    return sample * (Xcen.T @ Xcen)