# Exercise 41: Classifying Triangles

a=int(input("Enter the lengh of side a: "))
b=int(input("Enter the lengh of side b: "))
c=int(input("Enter the lengh of side c: "))

if a == b and b == c:
    Triangle="The Triangle is Equilateral"
elif a == b or b==c or c==a:
    Triangle="The Triangle is Isosceles"
elif a!=b or b!=c or c!=a:
    Triangle="The Triangle is Scaleno"
else:
    Triangle="Erorr, invalid data"

print (Triangle)
