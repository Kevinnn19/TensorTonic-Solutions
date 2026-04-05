import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    res = []
    for i in range(len(x)) :
        if x[i] > 0 :
            res.append(x[i])
        else :
            res.append(alpha * (math.exp(x[i]) - 1))
    return res