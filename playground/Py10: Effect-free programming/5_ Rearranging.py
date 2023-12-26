def rearrange(l):
    return sorted(l, key=lambda x: check(l,x))

def check(l,x):
    t = l.index(x)
    l[t] = "a"
    return (x > 0, t)
print(rearrange([2,5,2,5]))
"""def rearrange(l):
    non_positive = [x for x in l if x <= 0]
    positive = [x for x in l if x > 0]

    result = non_positive + positive
    
    return result"""