import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    true = np.asarray(y_true)
    pred = np.asarray(y_pred)
    n = len(true)
    tp = np.sum(true == pred)
    return float(tp/n)