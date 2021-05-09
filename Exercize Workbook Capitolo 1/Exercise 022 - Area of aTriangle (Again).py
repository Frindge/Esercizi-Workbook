# Exercise 22: Area of aTriangle (Again)

# l1, l2, l3 sono le lunghezze dei 3 lati del triangolo

import math

l1=float(input("inserire un numero da dare al lato1 del triangolo: "))
l2=float(input("inserire un numero da dare al lato2 del triangolo: "))
l3=float(input("inserire un numero da dare al lato3 del triangolo: "))
# formula data dall'esercizio
l=(l1+l2+l3)/2
# formula per l'area
area=math.sqrt(l*(l-l1)*(l-l2)*(l-l3))

print("l'area del triangolo è:%.2f" % area)
