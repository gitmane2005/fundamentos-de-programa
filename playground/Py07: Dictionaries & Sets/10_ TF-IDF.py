import math
def tfidf(documents):
    N = len(documents)
    string = " ".join(documents)
    string = string.lower()
    word_list = string.split()
    dic = {}
    not_repeated = []
    list(map(lambda x: not_repeated.append(x) if x not in not_repeated else None , word_list))
    
    def func_not_repeated(i):
        r = []
        for doc in documents:
            t = (doc.lower()).split()
            r.append(t.count(i))
        dic[i] = r.copy()
        r.clear()
    list(map(lambda x: func_not_repeated(x), not_repeated))

    for abc in dic.keys():
        n = 0
        for c in dic[abc]:
            if(c > 0):
                n += 1
        for c in range(N):
            dic[abc][c] = round(dic[abc][c]*math.log(N/n),3)

    return(dic)