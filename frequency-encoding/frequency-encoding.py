def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    cnts = {}
    for v in values :
        cnts[v] = cnts.get(v,0) + 1
    n = len(values)
    return [cnts[v]/n for v in values]