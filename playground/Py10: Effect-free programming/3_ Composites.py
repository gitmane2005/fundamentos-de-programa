def get_composites(t):
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
print(get_composites(6))