import math
def average(a, b):
    return math.ceil((a + b) / 2)

def digits_average(n):
    if len(n) == 0 or len(n) == 1:
        return n
    while n >= 10:
        avg = 0
        power = 0
        while n >= 10:
            avg = avg + average(n % 10, (n//10) % 10) * 10**power
            n //= 10
            power += 1
        n = avg
    return n
