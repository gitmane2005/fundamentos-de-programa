import math
def pascal(n):
    result = ""
    for i in range(n):
        i_factor = math.factorial(i)
        for j in range(i+1):
            j_factor = math.factorial(j)
            i_minus_j_factor = math.factorial(i-j)
            result = result + str(int(i_factor/(j_factor*i_minus_j_factor)))
            if i == n-1 == j:
                return result
            elif j == i:
                continue
            result = result +  " "
        result = result + "\n"
    return result