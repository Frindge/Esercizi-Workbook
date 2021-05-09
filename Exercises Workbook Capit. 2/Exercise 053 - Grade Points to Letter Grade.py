# Exercise 53: Grade Points to Letter Grade

# A+                4.0
# A                 4.0
# A-                3.7
# B+                3.3
# B                 3.0
# B-                2.7
# C+                2.3
# C                 2.0
# C-                1.7   1.5
# D+                1.3  1.15
# D                 1.0  0.5
# F                 0    

grade=float(input("Enter a value of voting points in number in this mode - 1.75: "))

if grade >= 4.0:
    letter="A+"
elif grade >=3.85:
    letter="A"
elif grade >=3.5:
    letter="A-"
elif grade >=3.15:
    letter="B+"
elif grade >=2.85:
    letter="B"
elif grade >=2.5:
    letter="B-"
elif grade >=2.15:
    letter="C+"
elif grade >=1.85:
    letter="C"
elif grade >=1.5:
    letter="C-"
elif grade >=1.15:
    letter="D+"
elif grade >=0.5:
    letter="D"
elif grade >=0:
    letter="F"
else:
    print("Error, Invalid data")
    


print("Of points %.2f the letter grade is %s" % (grade, letter))
