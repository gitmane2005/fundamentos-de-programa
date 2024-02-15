import collections
def most_frequent(alist):
    abc = collections.Counter(alist)

    max_apperance = max(abc.values())
    possible_result = []
    for (key,value) in abc.items():
        if value == max_apperance:
            possible_result.append(key)

    return max(possible_result)