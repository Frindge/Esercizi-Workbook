# Exercise 39: Month Name to Number of Days

month=str(input("Enter the name of month in this mode, April: "))
month=month.title()


if month == "April" or month == "June" or month == "September" or month == "November":
    month="%s have 30 days" % month
elif month == "February":
    month = "February have 28 days or 29 days in the leap year"
elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August"\
     or month == "October" or month == "December":
    month="%s have 31 days" % month
else:
    month="invalid data"


print(month)
