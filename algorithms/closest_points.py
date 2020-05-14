def find_closest_1d(input_points: list) -> tuple:
    """
    Given a 1D array/list of points, return the pair of points that are closest to each other, using Euclidean
    distance. Brute force would be O(n^2), but we first sort (n log n) and then iterate through the array (n) to give
    a total runtime of O(n log n).
    NOTE: if there are multiple sets of points with the same minimum distance between them, only a single pair of points
    is returned (the pair with lowest absolute value of the points themselves).
    For example, if input is [23, 4, 9, 16, 22, 1, 10] then return (9, 10)
    :param input_points: list, the input points [p1, p2, ....,]
    :return: (pi, pj), the pair of closest points
    """
    if len(input_points) < 2:
        return ()
    # sort the input list. This takes O(n log n) time
    input_points.sort()

    # now iterate, keep track of min distance. Closest points must be adjacent in sorted list.
    min_dist = input_points[1] - input_points[0]
    min_idx = 0
    for ii in range(len(input_points) - 1):
        dist = input_points[ii + 1] - input_points[ii]
        if dist < min_dist:
            min_dist = dist
            min_idx = ii

    return input_points[min_idx], input_points[min_idx + 1]
