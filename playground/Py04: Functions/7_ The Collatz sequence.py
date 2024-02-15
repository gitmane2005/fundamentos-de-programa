def collatz(n):
    result = f"{n}"
    var = n
    while n != 1:
        result = result + ","
        if n%2 == 0:
            n = n/2
            result = result + str(int(n))
        
        else:
            n = n*3 +1 
            result = result + str(int(n))
    return result
