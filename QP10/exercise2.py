def comprehensions(i, j):
    t = [x for x in range(i, j+1)if x%10 == 3 or x%10 == 8]
    s = tuple(round(x**(1/2), 2) for x in range(i, j+1))
    dic = {x: chr(x) for x in range(i, j+1)}
    return (t,s,dic)


def union_with(combine, dict1, dict2):
    all_keys = set(dict1.keys()) | set(dict2.keys())
    t = {key: combine(dict1.get(key, None), dict2.get(key, None)) for key in all_keys}

    return t