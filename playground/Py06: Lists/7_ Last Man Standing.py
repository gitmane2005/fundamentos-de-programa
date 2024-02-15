def last_man_standing(a_list, step):
    result = a_list.copy()
    i = 0
    while len(result) != 1:
        i += step
        while i-1 >= len(result):
            i -= len(result)
        result.pop(i-1)
        i = i-1

    return result[0]