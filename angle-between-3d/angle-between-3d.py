import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.asarray(v, dtype=float)
    w = np.asarray(w, dtype=float)
    vnorm = np.linalg.norm(v)
    wnorm = np.linalg.norm(w)
    if vnorm < 1e-10 or wnorm < 1e-10 :
        return np.nan
    cost = np.dot(v,w) / (vnorm * wnorm)
    cost = np.clip(cost, -1.0, 1.0)
    return np.arccos(cost)