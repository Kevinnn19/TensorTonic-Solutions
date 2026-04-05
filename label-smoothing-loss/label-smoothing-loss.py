import numpy as np

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    q = []
    pred = np.asarray(predictions)
    K = pred.size
    for i in range(K) :
        if i == target :
            q.append((1 - epsilon) + (epsilon / K))
        else :
            q.append(epsilon / K)
    loss = -np.sum(q * np.log(pred))
    return loss