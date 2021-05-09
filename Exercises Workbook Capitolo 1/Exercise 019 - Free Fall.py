# Creare un programma che determini la velocità di un oggetto quando colpisce il suolo. L'utente inserirà l'altezza
# da cui l'oggetto viene lasciato cadere in metri (m). Poiché l'oggetto viene lasciato cadere, la sua velocità
# iniziale è 0m/s. Supponiamo che l'accelerazione dovuta alla gravità sia 9,8m/s**2. per calcolare la velocità finale,
# vf, quando la velocità iniziale, vi, l'accelerazione, a, e la distanza, d, sono note.

import math

gravità=9.8**2

h=float(input("inserire l'altezza calcolata in metri: "))
# la vi velocità iniziale non viene calcolata essendo pari a 0
# formula matematica
vf=math.sqrt(2 * gravità * h)

print("l'ogetto colpirà il suolo alla velocità di %.2f" % vf, "metri al secondo")
