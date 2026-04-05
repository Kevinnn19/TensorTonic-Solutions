import numpy as np

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    pred = np.asarray(predictions, dtype = float)
    pred = np.clip(pred, 1e-9, 1.0)
    q = []
    K = pred.size
    for i in range(K) :
        if i == target :
            q.append((1 - epsilon) + (epsilon / K))
        else :
            q.append(epsilon / K)
    q = np.asarray(q)
    loss = -np.sum(q * np.log(pred))
    return loss