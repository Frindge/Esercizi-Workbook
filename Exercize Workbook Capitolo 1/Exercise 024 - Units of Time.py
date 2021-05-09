# Exercise 24: Units of Time 
giorni=int(input("inserire un numero intero valido di giorni: "))
ore=int(input("inserire un numero intero valido di ore: "))
minuti=int(input("inserire un numero intero valido di minuti: "))
secondi=int(input("inserire un numero intero valido di secondi: "))

# giorno in secondi
giorno=(86400*giorni)
#ora in secondi
ora=(3600*ore)
# minuto in secondi
minuto=(60*minuti)
# secondi in secondi
secondo=(1*secondi)

secondi_totali=giorno+ora+minuto+secondo

print("%d giorni,%d ore,%d minuti e %d secondi,il totale in secondi è: %d " %(giorni, ore, minuti, secondi, secondi_totali))




