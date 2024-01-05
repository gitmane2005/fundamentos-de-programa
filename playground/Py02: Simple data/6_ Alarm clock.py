hours = int(input())
minutes = int(input())

clock_minutes = (minutes + 51) % 60
if clock_minutes<10:
    clock_minutes = "0" + str(clock_minutes)

plus_hours = (minutes + 51) // 60
clock_hours = (hours + 6 + plus_hours) % 24
if clock_hours<10:
    clock_hours = "0" + str(clock_hours)

print(f"{clock_hours}:{clock_minutes}")