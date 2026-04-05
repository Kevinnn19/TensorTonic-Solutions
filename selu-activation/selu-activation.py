import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    x = np.asarray(x)
    s = []
    for i in range(len(x)) :     
        if x[i] > 0 :
            s.append(lam * x[i])
        else :
            s.append(lam * alpha * (np.exp(x[i]) - 1))
    return s