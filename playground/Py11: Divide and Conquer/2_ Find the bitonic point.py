def bitonic_point(f):
    x = f()
    return max(x)


print(bitonic_point(lambda: [2, 6, 10, 25, 270, 30, 25, 10, 0])) 