import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    a = np.asarray(anchor, dtype=float)
    p = np.asarray(positive, dtype=float)
    n = np.asarray(negative, dtype=float)
    if a.ndim == 1 :
        a = a.reshape(1, -1)
    if p.ndim == 1 :
        p = p.reshape(1, -1)
    if n.ndim == 1 :
        n = n.reshape(1, -1)
    dp = np.sum((a - p) ** 2, axis=1)
    dn = np.sum((a - n) ** 2, axis=1)
    loss = np.maximum(0, dp - dn + margin)
    return np.mean(loss)