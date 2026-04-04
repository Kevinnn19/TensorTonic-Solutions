def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stword = set(stopwords)
    return [token for token in tokens if token not in stword]