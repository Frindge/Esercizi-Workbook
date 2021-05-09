# Molte persone pensano alla loro altezza in piedi e pollici, anche in alcuni paesi che usano principalmente il
# sistema metrico. Scrivi un programma che legga un numero di piedi dall'utente, seguito da un numero di pollici.
# Una volta letti questi valori, il tuo programma dovrebbe calcolare e visualizzare il numero equivalente di centimetri.

# Suggerimento: un piede è 12 pollici. Un pollice è 2,54 centimetri.

# 1 piede equivalente a pollici
pollici=12

# 1 pollice equivalente a centimetri
centimetri=2.54

# richiesta dati da inserire tramite l'utente
piedi=float(input("inserisci il valore in piedi: "))
pollici1=float(input("inserisci il valore in pollici: "))

# conversione del primo input piedi in centimetri
a=(piedi*pollici*centimetri)

# conversione del secondo input in centimetri
b=(pollici1*centimetri)

# somma di tutti i centimetri che definisce l'altezza totale
altezza=print("la tua altezza è:", a+b ,"centimetri")



