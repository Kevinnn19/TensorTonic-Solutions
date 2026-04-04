import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    pred = np.asarray(y_pred, dtype = float)
    true = np.asarray(y_true, dtype = float)
    if pred.shape != true.shape:
        raise ValueError("Shapes must match")
    return float(np.mean((pred - true) ** 2))