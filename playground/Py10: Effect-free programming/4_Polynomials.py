import functools
def evaluate(a, x):
    return functools.reduce(lambda a,b: a+b,[a[i]*(x**i) for i in range(len(a))])

print(evaluate([1, 2, 4], 5))
