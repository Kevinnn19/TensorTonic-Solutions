def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.asarray(X)
    D = X.shape[1]
    return np.linalg.inv(X.T @ X + lam * np.eye(D)) @ (X.T @ y)