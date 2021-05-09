# La superficie della Terra è curva e la distanza tra i gradi di longitudine varia con la latitudine. Di conseguenza,
# trovare la distanza tra due punti sulla superficie della Terra è più complicato che usare semplicemente il teorema
# di Pitagora.
# Sia (t1,g1) e (t2,g2) la latitudine e la longitudine di due punti sulla superficie terrestre. La distanza tra questi
# punti, seguendo la superficie della Terra, in chilometri è:

# distance=6371.01×arccos(sin(t1)×sin(t2)+cos(t1)×cos(t2)×cos(g1−g2))

# Il valore 6371,01 nell'equazione precedente non è stato scelto a caso. È il raggio medio della Terra in chilometri.

# Crea un programma che permetta all'utente di inserire la latitudine e la longitudine di due punti sulla Terra in gradi.
# Il tuo programma dovrebbe visualizzare la distanza tra i punti, seguendo la superficie della terra, in chilometri.

# Suggerimento: le funzioni trigonometriche di Python operano in radianti. Di conseguenza,avrete bisogno di convertire
# l'input dell'utente da gradi a radianti prima di calcolare la distanza con la formula discussa in precedenza.
# Il modulo math contiene una funzione chiamata radians che converte da gradi a radianti.

import math

lta=float(input("inserire la prima latitudine: "))
ltb=float(input("inserire la seconda latitudine: "))
lga=float(input("inserire la prima longitudine: "))
lgb=float(input("inserire la seconda longitudine: "))
# conversione in radianti
lt1=math.radians(lta)
lt2=math.radians(ltb)
lg1=math.radians(lga)
lg2=math.radians(lgb)
# distanza finale
distanza=6371.01*math.acos(math.sin(lt1)*math.sin(lt2)+math.cos(lt1)*math.cos(lt2)*math.cos(lg1-lg2))
print("La distanza è di km", distanza)
