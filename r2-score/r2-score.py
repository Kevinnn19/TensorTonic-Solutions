import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    true = np.asarray(y_true)
    pred = np.asarray(y_pred)
    if np.all(true == true[0]) :
        if np.all(pred == true) :
            return 1.0
        else :
            return 0.0
    mean = np.mean(true)
    ssres = np.sum((true - pred) ** 2)
    sstot = np.sum((true - mean) ** 2)
    return float(1 - (ssres / sstot))