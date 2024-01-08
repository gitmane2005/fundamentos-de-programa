def division(a, b):
    try:
        res = a/b
        return ("{0}/{1} = {2} ".format(a,b, res))
    except ZeroDivisionError:
        return("can't divide by 0!")
    except TypeError:
        return("unsupported operand type(s) for division")

print(division(10, "2"))
