# La quantità di energia richiesta per aumentare la temperatura di un grammo di un materiale di un grado Celsius è
# la capacità termica specifica del materiale, C. La quantità totale di energia, q, richiesta per aumentare m grammi
# di un materiale di ΔT gradi Celsius può essere calcolata usando la formula:
# q=mCΔT
# Scrivi un programma che legga la massa di un po' d'acqua e il cambiamento di temperatura dall'utente. Il tuo programma
# dovrebbe visualizzare la quantità totale di energia che deve essere aggiunta o rimossa per ottenere il cambiamento di
# temperatura desiderato.

# Suggerimento: la capacità termica specifica dell'acqua è 4.186(J/g°C). Poiché l'acqua ha una densità di 1,0 grammi
# per millilitro, puoi usare grammi e millilitri in modo intercambiabile in questo esercizio.

# Estendete il vostro programma in modo che calcoli anche il costo del riscaldamento dell'acqua. L'elettricità è
# normalmente fatturata usando unità di kilowatt-ora piuttosto che di Joule. In questo esercizio, si dovrebbe assumere
# che l'elettricità costi 8,9 centesimi per chilowatt-ora. Usate il vostro programma per calcolare il costo della
# bollitura dell'acqua necessaria per una tazza di caffè.

# Suggerimento: avrai bisogno di cercare il fattore di conversione tra Joule e kilowatt-ora per completare l'ultima
# parte di questo esercizio.

# capacità termica specifica del materiale, C
# quantità totale di energia, q
# m grammi
# ΔT gradi Celsius

c=4186
m=float(input("inserisci la quantità di massa del materiale: "))
ΔT=float(input("inserisci la temperatura: "))
# formula indicata
q=(m*c*ΔT)
print("quantità totale di energia:" , q)

joule_in_kwh=2.7777e-7

# energia in kilowatt
q_kwh =q*joule_in_kwh
# l'elettricità costi 8,9
elettricità=8.9

costo = elettricità*q_kwh

print("il costo dell'energia è: %.2f cent" % costo)





