def solver(a, b, c):
    sqare_root = ((b**2) -(4*a*c))
    if sqare_root < 0:
        return []
    
    sol1 = (-b + sqare_root**(1/2))/(2*a)
    sol2 = (-b - sqare_root**(1/2))/(2*a)
    ret0 = min(sol1, sol2)
    ret1 = max(sol1,sol2)
    if ret0 == ret1:
        return [ret0]
    result = [ret0,ret1]

    return result