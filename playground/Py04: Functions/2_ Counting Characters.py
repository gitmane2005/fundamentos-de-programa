def count_chars(rand,chara):
    occurrences = 0
    for i in range(len(rand)):
        if rand[i] == chara:
            occurrences = occurrences + 1

    if occurrences == 0:
        return -1
    else:
        return occurrences