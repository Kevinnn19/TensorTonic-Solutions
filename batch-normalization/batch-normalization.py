import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    g = np.asarray(gamma, dtype=float)
    b = np.asarray(beta, dtype=float)
    if x.ndim == 2 :
        mu = np.mean(x, axis=0, keepdims=True)
        sigma = np.mean((x-mu) ** 2, axis=0, keepdims=True)
        xt = (x - mu) / np.sqrt(sigma + eps)
        return g * xt + b
    if x.ndim == 4 :
        mu = np.mean(x, axis=(0,2,3), keepdims=True)
        sigma = np.mean((x-mu) ** 2, axis=(0,2,3), keepdims=True)
        xt = (x - mu) / np.sqrt(sigma + eps)
        g = g.reshape(1,-1,1,1)
        b = b.reshape(1,-1,1,1)
        return g * xt + b