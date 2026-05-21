import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    labels = np.asarray(y)
    if labels.ndim != 1:
        raise ValueError("labels must be a 1D array")

    if num_classes is None:
        num_classes = np.max(labels) + 1

    if np.any(labels < 0) or np.any(labels >= num_classes):
        raise ValueError("labels contain invalid class indices")

    one_hot = np.zeros((labels.size, num_classes), dtype=np.float64)
    one_hot[np.arange(labels.size), labels] = 1
    return one_hot