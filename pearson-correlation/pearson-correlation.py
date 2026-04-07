import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 :
        return None
    if X.shape[0] < 2 :
        return None
    Xcen = X - np.mean(X, axis=0)
    Cov = (Xcen.T @ Xcen) / (X.shape[0] - 1)
    std = np.std(X, axis=0, ddof=1)
    deno = np.outer(std, std)
    corr = Cov / deno
    corr[deno==0] = np.nan
    mask = std != 0
    corr[mask, mask] = 1.0
    return corr