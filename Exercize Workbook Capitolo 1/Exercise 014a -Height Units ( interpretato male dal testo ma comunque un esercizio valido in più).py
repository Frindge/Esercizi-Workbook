# Molte persone pensano alla loro altezza in piedi e pollici, anche in alcuni paesi che usano principalmente il
# sistema metrico. Scrivi un programma che legga un numero di piedi dall'utente, seguito da un numero di pollici.
# Una volta letti questi valori, il tuo programma dovrebbe calcolare e visualizzare il numero equivalente di centimetri.

# Suggerimento: un piede è 12 pollici. Un pollice è 2,54 centimetri.

# 1 piede equivalente a pollici
pollici=12
# 1 pollice equivalente a centimetri
centimetri=2.54
# richiesta d'inserimento all'utente
piede=input("Inserisci un numero per definire l'unità di misura piede: ")
# conversione da stringa a float e assegnazione alla variabile piede1
piede1=float(piede)
# conversione da piede a pollici
pollici2=float(piede1*pollici)
# stampa a video i pollici
print(pollici2,"pollici")
# conversione da pollic a centimetri con variabile centimetri1 che viene killata dopo la stampa a video
centimetri1=print(pollici2*centimetri,"centimetri")

      



