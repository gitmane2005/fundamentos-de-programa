def closest_pair(points):
    points_sorted = sorted(points, key= lambda x: x[0] )
    
    split(points_sorted)
    

def split(sorted_points):
    half_len = len(sorted_points)//2
    left_points = sorted_points[:half_len+1]
    right_points = sorted_points[half_len:]
    if len(left_points) == 2 and len(right_points) == 2:
        return min()

print(closest_pair([(1256, 8483), (61, 2321), (9442, 4823), (1940, 700)]))