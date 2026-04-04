def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    prob = np.asarray(prob_distributions, dtype = float)
    N = prob.shape[0]
    sel_probs = prob[np.arange(N), actual_tokens]
    H = -np.mean(np.log(sel_probs))
    return float(np.exp(H))