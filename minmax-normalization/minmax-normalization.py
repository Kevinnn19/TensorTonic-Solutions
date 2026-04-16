import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        xmin = np.min(X)
        xmax = np.max(X)
        deno = max(xmax - xmin, eps)
        return (X - xmin) / deno
    xmin = np.min(X, axis=axis, keepdims=True)
    xmax = np.max(X, axis=axis, keepdims=True)
    deno = np.maximum(xmax - xmin, eps)
    return (X - xmin) / deno