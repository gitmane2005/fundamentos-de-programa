def union_with(combine, dict1, dict2):
    return dict2
print(sorted(union_with(lambda x,y:x+y, {'a':1, 'b':2}, {'a':3, 'c':4}).items()))