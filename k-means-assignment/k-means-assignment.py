def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    assign = []
    for p in points :
        bdist = float('inf')
        bidx = 0
        for j, c in enumerate(centroids) :
            dist = 0
            for d in range(len(p)) :
                dist += (p[d] - c[d]) ** 2
            if dist < bdist :
                bdist = dist
                bidx = j
        assign.append(bidx)
    return assign