import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    true = np.asarray(y_true, dtype = float)
    pred = np.asarray(y_pred, dtype = float)
    err = np.abs(true - pred)
    loss = np.where(err <= delta, 0.5 * (err ** 2), delta * (err - (0.5 * delta)))
    return np.mean(loss)