# Exercise 54: Assessing Employees

# 0.0                       Unacceptable Performance
# 0.4                       Acceptable Performance
# 0.6 or more               Meritorious Performance
a=2400
rating=float(input("Enter a rating for your employee: "))

if rating == 0.0:
    Meaning="Unacceptable"
    result=0.0
elif rating == 0.4:
    Meaning="Acceptable"
    result=2400*rating
elif rating == 0.6:
    Meaning="Meritorious"
    result=2400*rating
else:
    print("Error,insert this rating(0.0 - 0.4 - 0.6)")
    quit()
    
print("rating is %.1f,the performance is %s,the amount of an employee’s raise is $%.2f" % (rating, Meaning, result))
