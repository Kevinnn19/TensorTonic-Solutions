import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y = np.asarray(y_train)
    x = np.asarray(X_test)
    classes, cnts = np.unique(y, return_counts=True)
    majclass = classes[np.argmax(cnts)]
    pred = np.full(len(x), majclass, dtype=float)
    return pred