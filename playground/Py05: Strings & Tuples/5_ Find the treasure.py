def map(pos, steps):
    x = pos[0]
    y = pos[1]
    words = steps.split("-")
    for word in words:
        if word == "up":
            y += 1
        elif word == "down":
            y += -1
        
        elif word == "left":
            x += -1
        
        elif word == "right":
            x += 1

    return(x,y)