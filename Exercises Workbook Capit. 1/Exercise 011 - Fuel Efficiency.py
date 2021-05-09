# Negli Stati Uniti, l'efficienza del carburante per i veicoli è normalmente espressa in miglia per gallone (MPG).
# In Canada, l'efficienza del carburante è normalmente espressa in litri per cento chilometri (L/100km).
# Usa le tue capacità di ricerca per determinare come convertire da MPG a L/100km. Poi crea un programma che legga
# un valore dall'utente in unità americane e mostri l'equivalente efficienza del carburante in unità canadesi.

# MPG= miglia per gallone
# L/100km=litri per cento chilometri
# convertire da MPG a L/100km

litri_km=235.21  #1 l/100km in MPG

# MPG richiesti all'utente
MPG=float(input("Inserisci il quantitativo di carburante in MPG da convertire in unità Canadesi: "))

# conversione
litri_per_100km=(litri_km / MPG )
print("l'equivalente efficienza del carburante in unità canadesi sono: L/100km=",litri_per_100km)
