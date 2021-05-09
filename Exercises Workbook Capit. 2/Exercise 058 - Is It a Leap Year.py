# Exercise 58: Is It a Leap Year?

#• Any year that is divisible by 400 is a leap year.
#• Of the remaining years, any year that is divisible by 100 is not a leap year.
#• Of the remaining years, any year that is divisible by 4 is a leap year.
#• All other years are not leap years.

# Write a program that reads a year from the user and displays a message indicating
# whether or not it is a leap year.

years=int(input("Enter the year: "))
years=years % 400
years1=years % 4
years2=years % 100

if years2 == 0:
    print("no")
elif years == 0 or years1 == 0:
    print("is a leap year")
else:
    print("is not a leap year")
