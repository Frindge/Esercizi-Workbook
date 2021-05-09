# Exercise 59: Next Day

year=int(input("Enter year: "))
month=int(input("Enter month: "))
day=int(input("Enter day: "))
leap=year % 4

# new yaear
if month == 12 and day == 31:
    year=year+1
    month=month-11
    day=1

# February day 29    
elif month ==2 and day==29:
    month=month+1
    day=1

# February for lap year
elif month==2 and day==28:
    if leap == 0:
        day=29
    else:
        month=month+1
        day=1


# change month for month over 30 days
elif month == 4 and day ==30 or month == 6 and day ==30 or \
month == 9 and day ==30 or month == 11 and day ==30:
    month=month+1
    day=+1

# change month for month over 31 days
elif month == 1 and day ==31 or month == 3 and day ==31 or month == 5 and day ==31\
or month == 7 and day ==31 or month == 8 and day ==31 or month == 10 and day ==31:
    month=month+1
    day=+1

# limit month and limit days for error
elif month > 12 or day >31 or month <1 or day <1:
    print("Error, invalid data")
    quit()
else:
    day=day+1
    
print(year, month, day)
