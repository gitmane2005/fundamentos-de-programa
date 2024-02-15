def greatest(num):
    n = str(num)
    t = 1
    while t != 0:
        t = 0
        for i in range(len(n)-1):
            if int(n[i])< int(n[i+1]):
                n = n[:i] + n[i+1] + n[i] + n[i+2:]
                t += 1
            else:
                continue
        
    return int(n)