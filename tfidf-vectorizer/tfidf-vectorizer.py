import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    if not documents:
        return np.array([]), []

    tkn_docs = []
    for doc in documents:
        words = doc.lower().split()
        tkn_docs.append(words)

    vocab = sorted(set(word for doc in tkn_docs for word in doc))
    word_to_idx = {word: idx for idx, word in enumerate(vocab)}

    df = Counter()
    for doc in tkn_docs:
        unique_words = set(doc)
        for word in unique_words:
            df[word] += 1

    N = len(documents)
    idf = {}
    for word in vocab:
        idf[word] = math.log(N/df[word])

    tfidf_matrix = np.zeros((N, len(vocab)))
    for i, doc in enumerate(tkn_docs):
        if len(doc) == 0:
            continue
        termcnt = Counter(doc)
        totalwrd = len(doc)
        for word, cnt in termcnt.items():
            tf = cnt / totalwrd
            tfidf_score = tf * idf[word]
            col_idx = word_to_idx[word]
            tfidf_matrix[i][col_idx] = tfidf_score
    return tfidf_matrix, vocab