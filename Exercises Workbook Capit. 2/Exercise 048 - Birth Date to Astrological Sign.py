# Exercise 48: Birth Date to Astrological Sign

# Capricorn        December 22 to January 19
# Aquarius         January 20 to February 18
# Pisces           February 19 to March 20
# Aries            March 21 to April 19
# Taurus           April 20 to May 20
# Gemini           May 21 to June 20
# Cancer           June 21 to July 22
# Leo              July 23 to August 22
# Virgo            August 23 to September 22
# Libra            September 23 to October 22
# Scorpio          October 23 to November 21
# Sagittarius      November 22 to December 21

month=input("Enter one month in letters: ")
month=month.title()
day=int(input("Enter day in integer number: "))

if day <1 or day >31:
    print("Error, min day 1 max days 31")
elif month == "December" and day >=22 or month == "January" and day <=19:
    print("Capricorn")
elif month == "January" and day >=20 or month == "February" and day <=18:
    print("Aquarius")
elif month == "February" and day >29 :
    # limit days for February
    print("Error, form month February max days are 28 or 29 for leap year")
elif month == "February" and day >=19 or month == "February" and day <=29:
    print("Pisces")
elif month == "March" and day >=1 or month == "March" and day <=20:
    print("Pisces")
elif month == "March" and day >=21 or month == "April" and day <=19:
    print("Aries")
elif month == "April" and day >=20 or month == "May" and day <=20:
    print("Taurus")
elif month == "May" and day >=21 or month == "June" and day <=20:
    print("Gemini")
elif month == "June" and day >=21 or month == "July" and day <=22:
    print("Cancer")
elif month == "July" and day >=23 or month == "August" and day <=22:
    print("Leo")
elif month == "August" and day >=23 or month == "September" and day <=22:
    print("Virgo")
elif month == "September" and day >=23 or month == "October" and day <=22:
    print("Libra")
elif month == "October" and day >=23 or month == "November" and day <=21:
    print("Scorpio")
elif month == "November" and day >=22 or month == "December" and day <=21:
    print("Sagittarius")
else:
    print("There is something wrong with your data, please try again.")
