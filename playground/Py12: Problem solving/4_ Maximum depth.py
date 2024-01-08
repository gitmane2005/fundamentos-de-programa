def maximum_depth(l):
    return max(list(map(lambda x: maximum_depth(x) + 1, l)),1)
"""def maximum_depth(l):
    if l == []:
        return 1
    else:
        biggest = 0
        for x in l:
            biggest = max(biggest,maximum_depth(x))
        return (biggest +1)"""

print(maximum_depth([[[], [], [[]]], [[]], [], [[]]]))