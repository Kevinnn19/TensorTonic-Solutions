import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    mean = np.mean(x)
    med = np.median(x)
    cnts = Counter(x)
    maxfreq = max(cnts.values())
    mod = [val for val, freq in cnts.items() if freq == maxfreq]
    mode = float(min(mod))
    return mean, med, mode