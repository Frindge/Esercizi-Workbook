# Exercise 25: Units of Time (Again)


giorno=86400
ora=3600
minuti=60


secondi=int(input("inserisci la quantità di secondi da voler calcolare: "))

g=secondi/giorno
secondi=secondi % giorno

o=secondi/ora
secondi=secondi % ora

m=secondi/minuti
secondi=secondi % minuti

print("il calcolo è %d:%02d:%02d:%02d" % (g, o, m , secondi))

# la variabile secondi va ad essere sempre manipolata
