# Exercise 52: Letter Grade to Grade Points 

# A+                4.0
# A                 4.0
# A-                3.7
# B+                3.3
# B                 3.0
# B-                2.7
# C+                2.3
# C                 2.0
# C-                1.7
# D+                1.3
# D                 1.0
# F                 0

grade1=input("Enter a letter grade: ")
grade=grade1.title()

if grade == "A+" or grade == "A":
    print("the score is 4.0")
elif grade == "A-":
    print("the score is 3.7")
elif grade == "B+":
    print("the score is 3.3")
elif grade == "B":
    print("the score is 3.0")
elif grade == "B-":
    print("the score is 2.7")
elif grade == "C+":
    print("the score is 2.3")
elif grade == "C":
    print("the score is 2.0")
elif grade == "C-":
    print("the score is 1.7")
elif grade == "D+":
    print("the score is 1.3")
elif grade == "D":
    print("the score is 1.0")
elif grade == "F":
    print("the score is 0")
else:
    print("Error, Invalid data")
