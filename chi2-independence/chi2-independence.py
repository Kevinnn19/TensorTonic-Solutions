import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.asarray(C, dtype=float)
    row = np.sum(C, axis=1)
    col = np.sum(C, axis=0)
    expec = np.outer(row, col) / np.sum(C)
    chi2 = np.sum((C - expec) ** 2 / expec)
    return chi2, expec