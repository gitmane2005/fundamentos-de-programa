def pattern_hunting(l1, l2, p):
    result = []
    for i in l1:
        if p in i:
            result.append(l2[l1.index(i)])
    for i in l2:
        if p in i:
            result.append(l1[l2.index(i)])

    return sorted(result,reverse=True)