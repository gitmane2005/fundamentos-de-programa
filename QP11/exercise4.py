def bisect(f, n):
    lower = 0
    upper = 1
    midpoint = 0
    for x in range(n):
        midpoint = (lower + upper)/2
        if (f(lower)>=0 and f(midpoint)>=0) or (f(lower)<0 and f(midpoint)<0):
            lower = round(midpoint,6)
        else:
            upper = round(midpoint,6)
        
    
    return round(midpoint,5)
