import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.asarray(fpr, dtype=float)
    tpr = np.asarray(tpr, dtype=float)
    n = fpr.shape[0]
    aucarr = 0
    for i in range(n-1):
        aucarr += 0.5 * (tpr[i] + tpr[i+1]) * (fpr[i+1] - fpr[i])
    return aucarr