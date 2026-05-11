import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    ytrue = np.asarray(y_true)
    ypred = np.asarray(y_pred)
    acc = float(np.mean(ytrue == ypred))
    labels = np.unique(np.concatenate([ytrue, ypred]))
    precs = []
    recs = []
    f1s = []
    sups = []
    ttp = tfp = tfn = 0
    for c in labels :
        tp = np.sum((ytrue == c) & (ypred == c))
        fp = np.sum((ytrue != c) & (ypred == c))
        fn = np.sum((ytrue == c) & (ypred != c))
        sup = np.sum(ytrue == c)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        if prec + rec > 0:
            f1 = 2 * prec * rec / (prec + rec)
        else :
            f1 = 0.0
        precs.append(prec)
        recs.append(rec)
        f1s.append(f1)
        sups.append(sup)
        ttp += tp
        tfp += fp
        tfn += fn
    precs = np.asarray(precs)
    recs = np.asarray(recs)
    f1s = np.asarray(f1s)
    sups = np.asarray(sups)

    # Binary
    if average == "binary" :
        idx = np.where(labels == pos_label)[0][0]
        prec = precs[idx]
        rec = recs[idx]
        f1 = f1s[idx]

    # Micro
    elif average == "micro" :
        prec = ttp / (ttp + tfp) if (ttp + tfp) > 0 else 0.0
        rec = ttp / (ttp + tfn) if (ttp + tfn) > 0 else 0.0
        if prec + rec > 0 :
            f1 = 2 * prec * rec / (prec + rec)
        else :
            f1 = 0.0

    # Macro
    elif average == "macro" :
        prec = float(np.mean(precs))
        rec = float(np.mean(recs))
        f1 = float(np.mean(f1s))

    # Weighted
    elif average == "weighted" :
        w = sups / np.sum(sups)
        prec = float(np.sum(precs * w))
        rec = float(np.sum(recs * w))
        f1 = float(np.sum(f1s * w))

    else :
        raise ValueError("Invalid average mode")

    return {
        "accuracy" : float(acc),
        "precision" : float(prec),
        "recall" : float(rec),
        "f1" : float(f1)
    }