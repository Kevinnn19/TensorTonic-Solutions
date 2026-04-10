import numpy as np

def gini(y):
    if len(y) == 0 :
        return 0.0
    _, cnts = np.unique(y, return_counts=True)
    probs = cnts / cnts.sum()
    return float(1 - np.sum(probs ** 2))

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    left = np.asarray(y_left, dtype=float)
    right = np.asarray(y_right, dtype=float)
    NL = len(left)
    NR = len(right)
    N = NL + NR
    if N == 0 :
        return 0.0
    return float(NL * gini(left) / N + NR * gini(right) / N)