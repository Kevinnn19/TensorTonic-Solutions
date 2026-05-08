import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    v = np.asarray(V, dtype=float)
    vc = v.copy()
    delta = r + gamma * v[s_next] - v[s]
    vc[s] = v[s] + alpha * delta
    return vc