def longest_prefix(words):
    if len(words) == 1 or len(words) == "":
        return words[0]
    ln = round(len(words)/2)
    x = longest_prefix(words[:ln])
    y = longest_prefix(words[ln:])
    return merge(x,y)

def merge(lst1,lst2):
    t = list(zip(lst2,lst1))    
    i = 0
    c = []
    for x in t:
        if x[0] != x[1]:
            break
        c.append(x[0])
        i += 1
    return "".join(c)


#print(longest_prefix(['apple', 'apply', 'ape', 'april', "apph"]))
#print(longest_prefix(['sedatesingratiateconcomitant', 'sedatesparleypoliteness', 'sedateselbowsHahn', "sedatesgloweringimbecility's", 'sedatesbuttershexing', "sedatesKwangju'smulch's", 'sedatesunwiserN', 'sedatesprepossessedboggles', 'sedatesinterrelationshipdialings', "sedatesgropesNelsen's", 'sedatesMayfaircondemnations']))
#print(longest_prefix(['cahootsaffiliatedagglutinations', 'cahootslawnsrep', "cahootsSanka'sEwing", "cahootsdetection'simprovable", "cahootsVazquezChretien's", 'cahootsdevolvecrowded', 'cahootscudsdeterminant', 'cahootsfatheadhitches', 'cahootsthicknessesslow', "cahootssaying'soverreact", 'cahootsMethodistSherwood', 'cahootstackinessjourneyman', 'cahootsMoseleyreconsidering', "cahootspound'scondescendingly", 'cahootswellingtonhandsprings', "cahootsweekdayHussein's", "cahootsleitmotifssalmon's", 'cahootsgarrulitydefers', 'cahootsexplicitlyincapacitates', 'cahootsmaniafirst', 'cahootsgnomescosmetic', 'cahootselbowprotected']))