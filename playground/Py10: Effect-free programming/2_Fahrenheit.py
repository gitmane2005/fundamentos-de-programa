def to_fahr0enheit(t):
    dic_prime = {2,3}
    result = []
    for x in range(4,t+1):
        is_compositive = False
        for n in dic_prime:
            if x%n == 0:
                is_compositive = True
                break
        if is_compositive:
            result.append(x)
        else:
            dic_prime.add(x)
    return iter((result))
print(next(next(to_fahr0enheit(6))))