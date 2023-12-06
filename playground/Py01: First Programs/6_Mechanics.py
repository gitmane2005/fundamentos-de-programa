import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

time = ((18*sin_angle) / 5)
distance = cos_angle*18*time

print(round(distance))
