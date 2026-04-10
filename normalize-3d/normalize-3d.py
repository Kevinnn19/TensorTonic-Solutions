import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v, dtype=float)
    vnorm = np.linalg.norm(v, axis=-1, keepdims=True)
    vnorm = np.where(vnorm > 1e-10, vnorm, 1.0)
    vector = v / vnorm
    vector = np.where(vnorm > 1e-10, vector, 0.0)
    return vector