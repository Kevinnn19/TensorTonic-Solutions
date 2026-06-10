def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    res = []
    for i in range(len(values) - window_size + 1):
        wdw = sorted(values[i:i+window_size])
        n=len(wdw)
        if n % 2 == 1:
            median = float(wdw[n // 2])
        else:
            median = (wdw[n // 2 - 1] + wdw[n // 2]) / 2.0
        res.append(median)
    return res