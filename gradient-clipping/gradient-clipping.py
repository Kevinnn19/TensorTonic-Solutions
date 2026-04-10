import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g, dtype=float)
    if max_norm <= 0 :
        return g.copy()
    gnorms = np.linalg.norm(g)
    if gnorms == 0 :
        return g.copy()
    if gnorms > max_norm :
        g = g * (max_norm / gnorms)
    return g