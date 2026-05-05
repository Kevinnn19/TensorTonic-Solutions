import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.asarray(x)
    q = np.asarray(q)
    xsort = np.sort(x)
    res = np.percentile(xsort, q, method='linear')
    return res