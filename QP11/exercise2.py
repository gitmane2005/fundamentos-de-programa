def find_me(f, limits):
    average = (limits[0] + limits[1])//2
    eteration = 1
    while True:
        if f(average) == 0:
            return eteration
        elif f(average) == -1:
            limits = (limits[0], average-1)
        else:
            limits = (average+1, limits[1])
        average = (limits[0] + limits[1])//2
        eteration += 1
#print(find_me(lambda n: -1 if n > 30 else 1 if n < 30 else 0, (0, 100)))