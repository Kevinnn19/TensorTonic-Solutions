def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    unique = set(item for lst in recommendations for item in lst)
    return len(unique) / n_items