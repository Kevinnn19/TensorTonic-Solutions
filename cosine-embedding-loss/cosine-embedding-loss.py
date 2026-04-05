import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    dot = np.dot(x1,x2)
    norm1 = np.linalg.norm(x1)
    norm2 = np.linalg.norm(x2)
    if label == 1 :
        return 1 - dot / (norm1 * norm2)
    elif label == -1 :
        return np.maximum(0, (dot / (norm1 * norm2)) - margin)
    else :
        raise ValueError("Invalid label")