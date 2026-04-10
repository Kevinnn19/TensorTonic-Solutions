import numpy as np

def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    # Write code here
    w = np.asarray(w, dtype=float)
    g = np.asarray(grad, dtype=float)
    egs = np.asarray(E_grad_sq, dtype=float)
    eus = np.asarray(E_update_sq, dtype=float)
    egs = rho * egs + (1 - rho) * g ** 2
    wd = -(np.sqrt(eus + eps) / np.sqrt(egs + eps)) * g
    eus = rho * eus + (1 - rho) * wd ** 2
    w = w + wd
    return (w, egs, eus)