def gcd_rec(n1, n2):
    if min(n1, n2) == 0:
        return max(n1, n2)
    else:
        a = min(n1, n2)
        b = max(n1, n2)

        return gcd_rec(a, b-a)