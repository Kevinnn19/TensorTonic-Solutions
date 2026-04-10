import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    y = np.asarray(y)
    sm = np.asarray(split_mask)
    left = y[sm]
    right = y[~sm]
    NL = len(left)
    NR = len(right)
    N = len(y)
    if NL == 0 or NR == 0:
        return 0.0
    return _entropy(y) - (NL * _entropy(left) / N + NR * _entropy(right) / N)