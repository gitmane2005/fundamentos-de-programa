def find_length(n):
    length = 0
    while n != 0:
        length += 1
        n = n // 10 
    return length

def digits_average(n):
    while find_length(n) > 1:
        result = 0
        t = find_length(n) -1
        ind = 1
        for i in range(t):
            x = n%10
            n = n//10
            y = n%10
            result = int(((x+y)/2)+0.5)*ind + result
            ind = ind*10
        n = result

    return n