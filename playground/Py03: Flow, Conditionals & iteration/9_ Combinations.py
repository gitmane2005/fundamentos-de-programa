def C(n,r):
    result = faturial(n)/(faturial(r)*faturial(n-r))
    return int(result)
def faturial(i):
    t = 1
    while i > 0:
        t = i*t
        i = i - 1 
    return t
