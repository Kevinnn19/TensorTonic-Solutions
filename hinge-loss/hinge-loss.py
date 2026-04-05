import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    true = np.asarray(y_true, dtype = float)
    score = np.asarray(y_score, dtype = float)
    if true.shape != score.shape :
        raise ValueError("Shape must match")
    loss = np.maximum(0, margin - true * score)
    if reduction == "mean" :
        return float(np.mean(loss))
    elif reduction == "sum" :
        return float(np.sum(loss))
    else :
        raise ValueError("Invalid reduction type")