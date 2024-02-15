direction = {"RIGHT":"LEFT",
              "LEFT": "RIGHT",
              "UP": "DOWN",
              "DOWN": "UP"}

def min_path(path):
    result = []
    result.append(path[0])
    for now in path[1:]:
        
        if len(result)!= 0 and result[-1] == direction[now]:
            del result[-1]
            continue
        result.append(now)
    return result