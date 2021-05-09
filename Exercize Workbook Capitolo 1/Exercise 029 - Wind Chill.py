# Exercise 29: Wind Chill

Ta=float(input("inserisce il valore della temperatura dell'aria: "))
v=float(input("inserisci il valore della velocità del vento: "))

# formula indice di raffreddamento del vento
wci=13.12 + 0.6215 * Ta - 11.37 * (v**0.16) + 0.3965 + Ta * (v**0.16)

print("l'indice di raffreddamento del vento arrotondato al numero intero più vicino è: ", round(wci))

