import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    res = np.zeros(len(vocab), dtype = int)
    freq = {}
    for t in tokens :
        freq[t] = freq.get(t,0) + 1
    for i,word in enumerate(vocab) :
        res[i] = freq.get(word,0) 
    return res