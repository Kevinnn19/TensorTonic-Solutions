def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    res = series[:]
    for _ in range(order):
        res = [res[i] - res[i-1] for i in range(1, len(res))]
    return res