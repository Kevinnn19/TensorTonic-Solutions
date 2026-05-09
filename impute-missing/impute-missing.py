import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.asarray(X, dtype=float, copy=True)
    if X.ndim == 1:
        mask = np.isnan(X)
        if np.all(mask):
            fval = 0
        else:
            if strategy == 'mean':
                fval = np.mean(X[~mask])
            elif strategy == 'median':
                fval = np.median(X[~mask])
            else:
                raise ValueError("Strategy must be mean or median")
        X[mask] = fval
        return X
    rows, cols = X.shape
    for j in range(cols):
        col = X[:,j]
        mask = np.isnan(col)
        if np.all(mask):
            fval = 0
        else:
            if strategy == 'mean':
                fval = np.mean(col[~mask])
            elif strategy == 'median':
                fval = np.median(col[~mask])
            else:
                raise ValueError("Strategy must be mean or median")
        col[mask] = fval
        X[:,j] = col
    return X
        