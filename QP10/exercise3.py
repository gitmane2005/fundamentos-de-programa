def pythagoreans(a,b):
    t = ((x,y,z) for x in range(a, b) for y in range(a, b) for z in range(a, b) if (x**2 + y**2) == z**2 and x<=y)
    return list(t)