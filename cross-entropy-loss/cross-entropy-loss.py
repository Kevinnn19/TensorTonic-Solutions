import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    true = np.asarray(y_true)
    pred = np.asarray(y_pred)
    rows = np.arange(len(true))
    prob = pred[rows, true]
    loss = -np.log(prob)
    return np.mean(loss)