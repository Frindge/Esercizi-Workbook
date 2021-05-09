# Exercise 23: Area of a Regular Polygon

import math

s=float(input("inserisci la lunghezza di un lato: "))
n=int(input("inserisci il numero dei lati: "))

area=(n*s**2)/(4*math.tan(math.pi/n))

print("l'area del poligono regolare è: %.2f" % area)
