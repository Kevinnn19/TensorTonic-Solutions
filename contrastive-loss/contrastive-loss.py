import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    y = np.asarray(y, dtype=float)
    if a.ndim == 1 :
        a = a.reshape(1, -1)
    if b.ndim == 1 :
        b = b.reshape(1, -1)
    d = np.linalg.norm(a - b, axis=1)
    pos = y * d ** 2
    neg = (1 - y) * np.maximum(0, margin - d) ** 2
    loss = pos + neg
    if reduction == "mean" :
        return np.mean(loss)
    else :
        return np.sum(loss)