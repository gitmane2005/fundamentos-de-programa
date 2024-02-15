def get_positions(sentence,word_list):
    sentence_list = sentence.split()
    
    result = ""
    for i in sentence_list:
        t = 0
        for j in word_list:
            if i == j:
                result = result + str(t) + " "

            t += 1
    
    if len(result) != 4:
        return ""
    
    return result