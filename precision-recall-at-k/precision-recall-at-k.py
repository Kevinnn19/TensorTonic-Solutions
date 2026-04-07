def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    topk = recommended[:k]
    rset = set(relevant)
    hits = 0
    for item in topk :
        if item in rset :
            hits += 1
    prec = hits / k
    rec = hits / len(relevant)
    return [prec, rec]