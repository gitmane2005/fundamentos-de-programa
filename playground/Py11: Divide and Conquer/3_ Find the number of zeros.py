def count_zeros(f):
    t = f().count(0)
    return t
print(count_zeros(lambda: [1, 1, 1, 0, 0]))