def fib(n):
    two = 1
    result = [0]
    for i in range(0,n-1):
        current = result[i] + two
        result.append(current)
        two = result[i]
    
    return result