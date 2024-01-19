def no_consecutives1(k):
    if k == 1:
        return 2
    elif k == 2:
        return 3
    else:
        return no_consecutives1(k-1) + no_consecutives1(k-2)