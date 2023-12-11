def number_of_collisions(objects):
    hits = 0
    for a in range(len(objects)):
        for b in range(a+1,len(objects)):
            if colide(objects[a], objects[b]):
                hits += 1
    return hits

def colide(obj1, obj2):
    if obj2["x1"] > obj1["x2"] or obj2["y1"] > obj1["y2"]:
        return False
    elif obj1["x1"] > obj2["x2"] or obj1["y1"] > obj2["y2"]:
        return False
    return True