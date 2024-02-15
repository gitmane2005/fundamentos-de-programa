def count_until(tup):
    n = 0
    for t in tup:
        if type(t) == tuple:
            return n
        n += 1
    
    return -1 