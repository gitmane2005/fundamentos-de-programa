def greatest_member(a_tuple):

    scores = []
    for part in a_tuple:
        scores.append(score_calculater(part))


    best_score = scores.index(max(scores))

    return a_tuple[best_score]

def score_calculater(b_tuple):
    score = 0
    for i in b_tuple:
        if tuple == type(i):
            score += score_calculater(i)
            continue


        word = list(i)
        for char in word:
            score += ord(char)

    return score
