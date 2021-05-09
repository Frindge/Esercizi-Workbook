# Exercise 60:What Day of the Week Is January 1?

# day_of_the_week = (year + floor((year − 1) / 4) − floor((year − 1) / 100) + floor((year − 1) / 400)) % 7 

year=int(input("Enter year: "))

day_of_the_week = (year + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)) % 7

S="Sunday 1°January"
M= "Monday 1°January"
Tu= "Tuesday 1°January"
W= "Wednesday 1°January"
Th= "Thursday 1°January"
F= "Friday 1°January"
Sa= "Saturday 1°January"


if day_of_the_week == 0:
    day=S
elif day_of_the_week == 1:
    day=M
elif day_of_the_week == 2:
    day=Tu
elif day_of_the_week == 3:
    day=W
elif day_of_the_week == 4:
    day=Th
elif day_of_the_week == 5:
    day=F
elif day_of_the_week == 6:
    day=Sa
else:
    print("invalid data")



print("The day is %s" % day)
