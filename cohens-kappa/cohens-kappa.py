import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)
    n = len(rater1)
    matches = np.sum(rater1 == rater2)
    po = matches / n
    labels = set(rater1) | set(rater2)
    pe = 0.0
    for label in labels :
        p1 = np.sum(rater1 == label) / n
        p2 = np.sum(rater2 == label) / n
        pe += p1 * p2
    if pe == 1.0 : 
        return 1.0
    return (po - pe) / (1 - pe)