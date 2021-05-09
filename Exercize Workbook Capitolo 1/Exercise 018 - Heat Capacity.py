# Il volume di un cilindro può essere calcolato moltiplicando l'area della sua base circolare per la sua altezza.
# Scrivi un programma che legga il raggio del cilindro, insieme alla sua altezza, dall'utente e ne calcoli il volume.
# Visualizza il risultato arrotondato ad una cifra decimale.

# volume cilindro=πr**2*h

import math

r=float(input("inserisci un valore d'assegnare al raggio: "))
h=float(input("inserisci un valore d'assegnare all'altezza: "))

area=math.pi * r**2
volume=area*h

print("il volume del cilindro è: %.1f centimetri" % volume)

