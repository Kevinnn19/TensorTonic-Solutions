import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try :
        mat = np.asarray(matrix, dtype = float)
    except :
        return None
    if mat.ndim != 2 :
        return None
    if mat.size == 0 :
        return None
    if mat.shape[0] != mat.shape[1] :
        return None
    evals = np.linalg.eigvals(mat)
    idx = np.lexsort((evals.imag, evals.real))
    evals = evals[idx]
    return evals