# Exercise 38: Name That Shape

sides=int(input("Enter the number of sides minimum 3 , maximum 10: "))

if sides <3 or sides >10:
    sides="invalid data"
elif sides == 3:
    sides="Triangle"
elif sides == 4:
    sides="Square"
elif sides == 5:
    sides="Pentagon"
elif sides == 6:
    sides="Hexagon"
elif sides == 7:
    sides="Heptagon"
elif sides == 8:
    sides="Octagon"
elif sides == 9:
    sides="Nonagon"
else:
    sides="Decagon"
print(sides)
