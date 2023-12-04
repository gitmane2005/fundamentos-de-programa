def union_with(combine, dict1, dict2):
    #all_keys = set(dict1.keys() | dict2.items())
    t = {key: combine(value,dict2[key])  if key in dict2.keys() else value for key,value in dict1.items()}#
    list(map(lambda x: t.update({x[0]: x[1]}) if x[0] not in t.keys() else None, dict2.items()))
    return t

print(sorted(union_with(lambda x,y:x+y, {'a':1, 'b':2}, {'a':3, 'c':4}).items()))