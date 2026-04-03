import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a, dtype = float)
    b = np.asarray(b, dtype = float)
    if a.shape != b.shape:
        raise ValueError("a and b must have the same shape")
    dot = np.dot(a,b)
    norma = np.linalg.norm(a)
    normb = np.linalg.norm(b)
    if np.isclose(norma, 0.0) or np.isclose(normb, 0.0):
        return 0.0
    return float(dot / (norma * normb))