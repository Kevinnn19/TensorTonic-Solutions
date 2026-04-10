import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y, dtype=float)
    if y.size == 0 :
        return 0.0
    vals, cnts = np.unique(y, return_counts=True)
    probs = cnts / cnts.sum()
    probs = probs[probs>0]
    entropy = -np.sum(probs * np.log2(probs))
    return float(entropy)