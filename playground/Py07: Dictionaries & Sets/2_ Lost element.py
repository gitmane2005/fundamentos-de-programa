def lost_element(s1, s2):
    x = s1-s2
    y = s2-s1
    f = max([x,y])
    return f.pop()