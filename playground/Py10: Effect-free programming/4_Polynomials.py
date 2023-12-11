import functools
def evaluate(a, x):
    """result = 0
    for i in range(len(a)):
        result = result + a[i]*(x**i)"""
    return functools.reduce(lambda a,b: a+b,[a[i]*(x**i) for i in range(len(a))])

print(evaluate([1, 2, 4], 5))
