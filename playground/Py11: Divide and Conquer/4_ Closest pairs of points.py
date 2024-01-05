def closest_pair(points):
    points_sorted = sorted(points, key= lambda x: x[0] )
    half_len = len(points_sorted)//2
    left_points = points_sorted[:half_len]
    right_points = points_sorted[half_len:]
    print(left_points)
    return right_points
print(closest_pair([(1256, 8483), (61, 2321), (9442, 4823), (1940, 700)]))