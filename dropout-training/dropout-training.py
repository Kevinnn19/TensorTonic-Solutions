import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x)
    if p == 0.0 :
        pattern = np.ones_like(x)
        return x.copy(), pattern
    if rng is not None:
        rndval = rng.random(x.shape)
    else:
        rndval = np.random.random(x.shape)
    mask = rndval < (1-p)
    sc = 1.0 / (1 - p)
    pattern = mask.astype(x.dtype) * sc
    out = x * pattern
    return out, pattern