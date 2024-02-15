def interval(n):
    lower = 0 
    upper = n
    midpoint = (upper + lower)/2
    midpoint_square = midpoint * midpoint
    while n != round(midpoint_square,5):
        if midpoint_square > n:
            upper = midpoint
        elif midpoint_square < n:
            lower = midpoint
        midpoint = (upper + lower)/2
        midpoint_square = midpoint * midpoint
    print(round(midpoint,5))
    
n = float(input())
interval(n)