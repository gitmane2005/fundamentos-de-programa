def rearrange(l):
    return sorted(l, key=lambda x: check(l,x))

def check(l,x):
    t = l.index(x)
    l[t] = "a"
    return (x > 0, t)
