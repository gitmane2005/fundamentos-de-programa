def maximum_depth(l):
    if l == []:
        return 1
    else:
        biggest = 0
        for x in l:
            biggest = max(biggest,maximum_depth(x))
        return (biggest +1)

print(maximum_depth([[[], [], [[]]], [[]], [], [[]]]))