def lfsr(n):
    n_original = n
    result = str(n[-1])
    n = xor(n[-2]+n[-1]) + n[:len(n)-1]
    while n != n_original:
        result += str(n[-1])
        n = xor(n[-2]+n[-1]) + n[:len(n)-1]
    return result

def xor(n):
    if n[0] != n[1]:
        return "1"
    else:
        return "0"