def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    k = len(weights)
    wsum = sum(weights)
    res = []
    for i in range(len(values) - k + 1):
        weightsum = sum(weights[j] * values[i+j] for j in range(k))
        res.append(weightsum / wsum)
    return res