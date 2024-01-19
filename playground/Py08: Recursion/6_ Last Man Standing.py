def last_man_standing(alist, step):
    return last_man_standing1(alist, step, 0)

def last_man_standing1(alist, step, last_index):
    if len(alist) == 1:
        return alist[0]
    else:
        if (step-1) + (last_index) >= len(alist):
            t = ((step-1) + (last_index))%len(alist)
            alist.pop(t)
            return last_man_standing1(alist, step, t)
        t = (step-1) + (last_index)
        alist.pop(t)
        return last_man_standing1(alist, step, t)