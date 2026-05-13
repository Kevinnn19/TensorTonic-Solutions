import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    log_fact = np.sum(np.log(np.arange(1,k+1))) if k > 0 else 0
    pmf = np.exp(-lam + k * np.log(lam) - log_fact)
    cdf = 0.0
    for i in range(k+1):
        log_fact = np.sum(np.log(np.arange(1,i+1))) if i > 0 else 0
        cdf += np.exp(-lam + i * np.log(lam) - log_fact)
    return pmf, cdf