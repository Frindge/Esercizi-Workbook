# Exercise 45: Date to Holiday Name

# New Yeaar's Day         January 1 
# Canada Day              July 1 
# Christmas Day           December 25

a="January 1"
b="July 1"
c="December 25"
data=str(input("Enter month in letters and day in number es(July 7). "))


if data==a:
    Fest="New Year’s Day"
elif data==b:
    Fest="Canada Day"
elif data==c:
    Fest="Christmas Day"
else:
    print("Error, invalid data")
    quit()

print("%s is %s " % (data, Fest))
