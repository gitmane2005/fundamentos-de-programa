def teste():
    le = int(input())
    re = int(input())
    pe = int(input())
    te = int(input())

    for i in [le, re, pe , te]:
        if i < 0 or i > 100:
            print("Input error")
            return 
    if pe<40 or te<40:
        print("RFF")
        return 
    else:
        grade =(le + re + 13 * pe + 5 * te) / 100
        grade_roundhalf_up = int(grade + 0.5)
        print(grade_roundhalf_up)

teste()