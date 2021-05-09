# Scrivi un programma che inizia leggendo un raggio, r, dall'utente. Il programma continuerà calcolando e visualizzando
# l'area di un cerchio con raggio r e il volume di una sfera con raggio r. Usate la costante pi greco nel modulo
# di matematica nei vostri calcoli.

# Suggerimento: l'area di un cerchio si calcola con la formula area=πr**2. Il volume di una sfera si calcola con
# la formula volume =(4 πr**3)/3

import math

r=float(input("Inserisci un valore da dare al raggio r: "))

area=math.pi * r**2
print("l'area del cerchio è: %.2f" % area)

volume=(math.pi *r**3)/3
print("il volume della sfera è: %.2f" % volume)
