def biggest_member(atuple):
    if not (type(atuple) is tuple):
        return atuple
    
    len_baybe_biggest = len(atuple)
    baybe_biggest = atuple
    for elemt in atuple:
        if type(elemt) is tuple:
            if len(biggest_member(elemt))>len_baybe_biggest:
                baybe_biggest =  biggest_member(elemt)
                len_baybe_biggest = len(baybe_biggest)
    
    return baybe_biggest