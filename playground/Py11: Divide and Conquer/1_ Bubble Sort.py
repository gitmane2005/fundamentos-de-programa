def bubble_sort(alist):
    change = True
    while change:
        change = False
        for x in range(len(alist)-1):
            if alist[x] > alist[x+1]:
                t = alist[x]
                alist[x] = alist[x+1]
                alist[x+1] = t
                change = True
    return alist
print(bubble_sort([5, 1, 2, 8, 2.5]))