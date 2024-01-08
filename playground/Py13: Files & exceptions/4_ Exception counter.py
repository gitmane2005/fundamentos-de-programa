def count_exceptions(f, n1, n2):
    result = 0
    for x in range(n1, n2+1):
        try:
            f(x)
        except:
            result += 1
    return result