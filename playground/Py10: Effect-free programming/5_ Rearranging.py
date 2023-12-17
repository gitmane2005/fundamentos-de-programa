def rearrange(l):
    pos = []
    neg = []
    for x in l:
        if x >= 0:
            pos.append(x)
        else:
            neg.append(x)

    return neg+pos

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))