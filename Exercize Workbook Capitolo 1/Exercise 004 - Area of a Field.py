# Creare un programma che legga dall'utente la lunghezza e la larghezza
# del campo di un agricoltore in piedi. Visualizza l'area del campo in acri.

# Suggerimento: ci sono 43.560 piedi quadrati in un acro. (sqft=piede quadrato)

lunghezza=float(input("inserisci la lunghezza del campo in piedi: "))
larghezza=float(input("inserisci la larghezza del campo in piedi: "))

sqftacri=43560

area_in_acri=lunghezza*larghezza/sqftacri

print("l'area del campo è di",area_in_acri,"acri")
