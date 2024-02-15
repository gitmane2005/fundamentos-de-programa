def first(r,s,l):
    if s > r:
        second(r,s,l)
        return
    r = r-s
    first(r,s,l)

def second(r,s,l):
    if r == 0:
        print(s)
        return
    else:
        m = l
        l = r
        r = s 
        s = l
        first(r,s,l)


l = int(input())
s = int(input())
r = l

if r < s:
    t = l 
    l = r
    r = s
    s = t
first(r,s,l)