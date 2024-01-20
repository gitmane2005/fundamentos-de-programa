def permutations(atuple):
    result = set()
    if len(atuple) == 1:
         return {atuple}
    elif len(atuple) <= 2:
        return {atuple, (atuple[1], atuple[0])}
    else:
        for x in permutations(atuple[1:]):
            for i in range(len(x)+1):
                result.add(tuple(list(x[:i]) + [atuple[0]] + list(x[i:])))
    return set(result)