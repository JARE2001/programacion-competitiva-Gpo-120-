ndays =int(input())

days= input().split()
rest=0

for day in range(len(days)):
    if days[day] == '0':
        rest+=1
    elif days[day] == '1' and day>0:
        if days[day-1] == '1':
            days[day] = '0'
            rest+=1
    elif days[day] == '2' and day>0:
        if days[day-1] == '2':
            days[day] = '0'
            rest+=1
    elif days[day] == '3' and day>0:
        if days[day-1] == '2':
            days[day] = '1'
        if days[day-1] == '1':
            days[day] = '2'

print(rest)