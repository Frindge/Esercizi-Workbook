# Exercise 47: Season from Month and Day

# Spring        March 20
# Summer        June 21
# Fall          September 22
# Winter        December 21

month=input("Enter one month in letters: ")
month=month.title()
day=int(input("Enter day in integer number: "))

if month=="March" and day >=20 and month=="March" and day <=31:
    print("The season is Spring")
elif month=="April" and day>=1 and month=="April" and day <=30:
    print("The season is Spring")
elif month == "May" and day >=1 and month=="May" and  day <=31:
    print("The season is Spring")
elif month == "June" and day >=1 and month=="June" and  day <=21:
    print("The season is Spring")
elif month == "June" and day >=22 and month == "June" and day <=30:
    print("The season is Summer")
elif month == "July" and day >=1 and month == "July" and day <=31:
    print("The season is Summer")
elif month == "August" and day >=1 and month == "August" and day <=31:
    print("The season is Summer")
elif month == "September" and day >=1 and month=="September" and  day <=22:
    print("The season is Summer")
elif month == "September" and day >=23 and month=="September" and  day <=30:
    print("The season is Fall")
elif month == "October" and day >=1 and month=="October" and  day <=31:
    print("The season is Fall")
elif month == "November" and day >=1 and month=="November" and  day <=30:
    print("The season is Fall")
elif month == "December" and day >=1 and month=="December" and  day <=21:
    print("The season is Fall")
elif month == "December" and day >=22 and month=="December" and  day <=31:
    print("The season is Winter")
elif month == "January" and day >=1 and month=="January" and  day <=31:
    print("The season is Winter")
elif month == "February" and day >=1 and month=="February" and  day <=29:
    print("The season is Winter")
elif month=="March" and day >=1 and month=="March" and day <=19:
    print("The season is Winter")
else:
    print("Erro,invalid data. The correct data are this mode - March 3")


