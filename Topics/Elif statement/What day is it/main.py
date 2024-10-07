def day_of_week_according_to_gmt(time1):
    days = ['Monday', 'Tuesday', 'Wednesday']
    time_london = 10.50
    if time_london + time1 >= 24:
        return days[2]
    elif time_london + time1 < 0:
        return days[0]
    else:
        return days[1]

time = int(input())
print(day_of_week_according_to_gmt(time))