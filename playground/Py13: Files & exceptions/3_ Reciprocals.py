def reciprocals(alist):
    result = []
    for x in alist:
        try:
            result.append(1/x)
        except:
            continue
    return result
