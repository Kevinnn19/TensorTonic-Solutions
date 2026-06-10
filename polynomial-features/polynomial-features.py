def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    res = []
    for val in values:
        ans = []
        for i in range(degree+1):
            ans.append(val ** i)
        res.append(ans)
    return res