from math import sqrt
import time
def closest_pair(points):
    #timer to check the run time for fun
    start = time.time()
    points_sorted = sorted(points, key= lambda x: x[0] )
    t =  split(points_sorted)
    end = time.time()
    print(end - start)
    return t
    
def split(sorted_points):
    if len(sorted_points) <= 1:
        return sorted_points
    elif len(sorted_points) == 2:
        p1 = sorted_points[0]
        p2 = sorted_points[1]
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    half_len = len(sorted_points)//2
    left_points = sorted_points[:half_len+1]
    right_points = sorted_points[half_len:]
    dl = split(left_points)
    dr = split(right_points)
    dLR = min(dl,dr)
    for x in left_points:
        for y in right_points:
            if x == y:
                continue
            if abs(x[0]- y[0]) < dLR:
                dist = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
                dLR = min(dLR, dist)
    return(round(dLR))
print(closest_pair([(1256, 8483), (61, 2321), (9442, 4823), (1940, 700)]))


#linear shearch for min distance 
"""minimun = 8293894829849823894892384982398498239
    min_point = ()
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            else:
                minimun1 = minimun
                minimun = min(minimun, sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
                if minimun != minimun1:
                    min_point = (p1,p2)
    print (min_point)
    return minimun"""
