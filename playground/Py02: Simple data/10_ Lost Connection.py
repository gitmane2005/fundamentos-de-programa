import math
def time_until_lost_connection(direction_A, direction_B):
    # my code here
    pi = math.pi
    angle = ((abs(direction_A - direction_B) / 2)*pi) / 180
    print(angle)
    walking = 17.5/math.sin(angle)
    print(walking)

    time = round((walking/5) * 60, 3)
    
    return time