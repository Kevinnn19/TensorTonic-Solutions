def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    L = (6 / (fan_in + fan_out)) ** 0.5
    result = []
    for row in W :
        new = []
        for val in row :
            new.append(val * 2 * L - L)
        result.append(new)
    return result