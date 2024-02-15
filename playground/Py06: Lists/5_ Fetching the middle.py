def fetch_middle(llists):
    result = []
    for list in llists:
        list_len = len(list)
        if list_len % 2 == 0:
            x1 = int(list_len/2)-1
            x2 = int(list_len/2)
            t = (list[x1]+list[x2])/2
            result.append(t)
        else:
            t = list[int(list_len/2)]
            result.append(t)

    return result