import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    if not docs:
        return np.array([])

    N = len(docs)
    doclen = np.array([len(doc) for doc in docs])
    avgdl = np.mean(doclen)

    df = Counter()
    for doc in docs:
        uword = set(doc)
        for word in uword:
            df[word] += 1

    idf = {}
    for word, freq in df.items():
        idf[word] = math.log(((N - df[word] + 0.5) / (df[word] + 0.5)) + 1)

    scores = np.zeros(N)
    unique_query = list(dict.fromkeys(query_tokens))
    for i, doc in enumerate(docs):
        tf = Counter(doc)
        doc_len = len(doc)
        score = 0
        for term in unique_query:
            if term not in idf:
                continue
            term_freq = tf.get(term, 0)
            if term_freq == 0:
                continue
            num = term_freq * (k1 + 1)
            deno = (term_freq + k1 * (1 - b + b * (doc_len/avgdl)))
            score += idf[term] * (num / deno)
        scores[i] = score
    return scores