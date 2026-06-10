def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    res = []
    for row in X:
        nrow = list(row)
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                nrow.append(row[i] * row[j])
        res.append(nrow)
    return res