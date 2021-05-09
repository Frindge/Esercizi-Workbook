# Exercise 25: Units ofTime (Again)


giorno=86400
ora=3600
minuti=60


secondi=int(input("inserisci la quantità di secondi da voler calcolare: "))

s=secondi//giorno
resto_s=secondi % 86400
print("il calcolo è %d giorni e %d secondi" % (s , resto_s))

o=secondi//ora
resto_o=secondi % 3600
print("il calcolo è %d ore e %d secondi" % (o , resto_o))

m=secondi//minuti
resto_m=secondi % 60
print("il calcolo è %d minuti e %d secondi" % (m , resto_m))
