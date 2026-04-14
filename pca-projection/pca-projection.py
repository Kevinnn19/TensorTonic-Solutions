import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    n = X.shape[0]
    Xcen = X - np.mean(X, axis=0)
    cov = (Xcen.T @ Xcen) / (n - 1)
    egnvals, egnvecs = np.linalg.eigh(cov)
    idx = np.argsort(egnvals)[::-1]
    egnvecs = egnvecs[:,idx]
    W = egnvecs[:, :k]
    Xproj = Xcen @ W
    return Xproj.tolist()