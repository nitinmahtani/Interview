def minimum_points(threshold, points):
    # write your code here
    if not points:
        return 0
    if threshold == 0:
        return 0
    if len(points) == 1:
        return 1
    must_be = 0
    i = 0
    count = 0
    while must_be < threshold and i < len(points) - 2:
        if points[i + 1] - points[0] > points[i + 2] - points[0]:
            must_be = points[i + 1] - points[0]
            i += 1
        else:
            must_be = points[i + 2] - points[0]
            i += 2
        count += 1
    return count + 1


if __name__ == "__main__":
    # write your debug code here
    pass
