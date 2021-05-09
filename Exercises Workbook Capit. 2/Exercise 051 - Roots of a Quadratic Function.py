# Exercise 51: Roots of a Quadratic Function
import math

a=float(input("Enter the value a: "))
b=float(input("Enter the value b: "))
c=float(input("Enter the value c: "))

discriminant = (b**2) - (4 * a * c)

print(discriminant)

if discriminant < 0:
    print("has no real roots")

elif discriminant == 0:
    result = (-b / (2 * a))
    print(result)
else:
    root1 = (- b - math.sqrt(discriminant)) / (2 * a)
    root2 = (- b + math.sqrt(discriminant)) / (2 * a)
    print("the first root is:", root1)
    print("the second root is:", root2)
