# In questo esercizio, creerete un programma che inizia leggendo una misura in piedi dall'utente. Poi il vostro
# programma dovrebbe visualizzare la distanza equivalente in pollici, yarde e miglia. Usate Internet per cercare i
# fattori di conversione necessari se non li avete memorizzati.

piedi=float(input("inserisci una misura in piedi: "))

# 1 piede in pollici
pollici=12
# 1 piede in yarde
yard=0.333333
# 1 piede in miglia 
miglia=0.000189394

# conversione in pollici, yard e miglia
in_pollici=print(float(piedi*pollici),"pollici")
in_yarde=print(float(piedi*yard),"yard")
in_miglia=print(float(piedi*miglia),"miglia")

# -------------------------------------------------------------------------------------------
# oppure,secondo modo di risolverlo con 2 lineein meno di codice 

# piedi=float(input("inserisci una misura in piedi: "))

pollici1=piedi*12
yard1=piedi*0.333333
miglia1=piedi*0.000189394

print("La distanza è: pollici %.2f , yard %.2f , miglia %.2f " %(pollici1, yard1, miglia1))


