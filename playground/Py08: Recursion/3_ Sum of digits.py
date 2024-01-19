def sum_digits_rec(n):
    if len(str(n)) == 1:
        return n
    else:
        
        return int(str(n)[0]) + sum_digits_rec(int(str(n)[1:]))
