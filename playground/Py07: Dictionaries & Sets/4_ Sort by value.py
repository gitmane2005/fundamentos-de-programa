def sort_by_value(dict):
    a = sorted(dict.values())
    for (key,value) in dict.items():
        index = a.index(value)
        a[index] = (key, value)
    
    return a