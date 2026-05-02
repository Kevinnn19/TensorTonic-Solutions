import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    mean = np.mean(x)
    xl = len(x)
    var = np.sqrt(np.sum((x - mean) ** 2) / (xl - 1))
    num = mean - mu0
    deno = var / np.sqrt(xl)
    return num / deno