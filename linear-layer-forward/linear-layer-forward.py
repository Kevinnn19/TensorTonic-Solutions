def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    n = len(X)
    din = len(X[0])
    dout = len(W[0])
    Y = []
    for i in range(n) :
        row = []
        for j in range(dout) :
            s = 0
            for k in range(din) :
                s += X[i][k] * W[k][j]
            s += b[j]
            row.append(s)
        Y.append(row)
    return Y