def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    freq = {}
    for sen in sentences :
        for word in sen :
            freq[word] = freq.get(word,0) + 1
    return freq