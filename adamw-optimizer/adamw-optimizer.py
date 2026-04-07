import numpy as np

def adamw_step(w, m, v, g, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    # Write code here
    w = np.asarray(w, dtype = float)
    m = np.asarray(m, dtype = float)
    v = np.asarray(v, dtype = float)
    g = np.asarray(g, dtype = float)
    m = beta1 * m + (1 - beta1) * g
    v = beta2 * v + (1 - beta2) * g * g
    w = w - lr * (weight_decay * w) - lr * m / (np.sqrt(v) + eps)
    return w, m, v