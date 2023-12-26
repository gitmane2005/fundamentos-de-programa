def batch_norm(alist, batch_size):
    batch_list = []
    while alist != []:
        batch_list.append(normalise(alist[:batch_size]))
        alist = alist[batch_size:]
    return iter(batch_list)
def normalise(alist):
    t = sorted(alist)
    mid = len(t) // 2
    medium = (t[mid] + t[~mid]) / 2
    t = list(map(lambda x: x-medium,alist))
    return t
