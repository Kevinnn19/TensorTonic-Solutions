import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    labels = np.asarray(labels, dtype=float)
    n = len(X)
    diff = X[:, None, :] - X[None, :, :]
    dist = np.sqrt(np.sum(diff ** 2, axis = 2))
    clusters = np.unique(labels)
    sh = []
    for i in range(n):
        #Intra cluster
        samedis = labels == labels[i]
        samedis[i] = False
        if np.sum(samedis) == 0:
            a = 0.0
        else :
            a = np.mean(dist[i, samedis])

        #Inter cluster
        b = np.inf
        for c in clusters:
            if c == labels[i]:
                continue
            mask = labels == c
            b = min(b, np.mean(dist[i, mask]))
        s = (b - a) / max(a, b)
        sh.append(s)
    return float(np.mean(sh))            