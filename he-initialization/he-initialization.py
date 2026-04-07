def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    L = (6 / fan_in) ** 0.5
    result = []
    for row in W :
        new = []
        for val in row :
            new.append(val * 2 * L - L)
        result.append(new)
    return result