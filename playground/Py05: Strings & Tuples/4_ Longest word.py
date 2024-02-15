def longest(s):
    s = s.split()
    res = ""
    for word in s:
        if len(word) > len(res):
            res = word
    return len(res)