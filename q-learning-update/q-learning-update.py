import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.asarray(Q, dtype=float)
    Qn = Q.copy()
    td = r + gamma * np.max(Q[s_next]) - Q[s][a]
    Qn[s][a] = Q[s][a] + alpha * td
    return Qn