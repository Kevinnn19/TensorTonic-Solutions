import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    erf_func = np.vectorize(math.erf)
    return 0.5 * x * (1 + erf_func(x / np.sqrt(2)))