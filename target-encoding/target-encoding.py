def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    sums = {}
    cnts = {}

    for cat, tar in zip(categories, targets):
        sums[cat] = sums.get(cat, 0) + tar
        cnts[cat] = cnts.get(cat, 0) + 1

    return [sums[cat] / cnts[cat] for cat in categories]