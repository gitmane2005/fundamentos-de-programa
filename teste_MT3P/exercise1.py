#15 min
def days_until_christmas(date):
    days_of_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31}
    present_day = (date[0], date[1], date[2])
    days_until_christmas_count = 0
    while (present_day[0], present_day[1]) != (25, 12):
        if days_of_month[present_day[1]] == present_day[0] and present_day[1] == 12:
            present_day = (1,1, present_day[2]+1)
            days_until_christmas_count += 1
        elif days_of_month[present_day[1]] == present_day[0]:
            present_day = (1, present_day[1]+1, present_day[2])
            days_until_christmas_count += 1
        else:
            present_day = (present_day[0]+1, present_day[1], present_day[2])
            days_until_christmas_count += 1
    return days_until_christmas_count
