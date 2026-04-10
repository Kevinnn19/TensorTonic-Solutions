def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    if len(recommendations) == 0 :
        return 0.0
    hits = 0;
    total = len(recommendations)
    for recs, truth in zip(recommendations, ground_truth) :
        topk = recs[:k]
        if set(topk) & set(truth) :
            hits += 1
    return hits / total