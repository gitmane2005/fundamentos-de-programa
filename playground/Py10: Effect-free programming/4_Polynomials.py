def evaluate(a, x):
    t = [a[i]*(x**i) for i in range(len(a))]
    return sum(t)

print(evaluate([1, 2, 4], 5))
