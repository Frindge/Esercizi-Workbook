# Il programma che creerete per questo esercizio inizierà leggendo il costo di un pasto ordinato in un ristorante
# dall'utente. Poi il programma calcolerà le tasse e la mancia per il pasto. Usate l'aliquota locale per calcolare
# l'ammontare delle tasse dovute. Calcolate la mancia come il 18% dell'importo del pasto (senza le tasse).
# L'output del tuo programma dovrebbe includere l'importo delle tasse, l'importo della mancia, e il totale complessivo
# del pasto che include sia le tasse che la mancia. Formattate l'output in modo che tutti i valori siano visualizzati
# con due cifre decimali.

mancia=18/100 #18%
tassa=5/100   #5%

pasto=int(input("il costo del pasto ordinato è: "))

# calcolo della mancia senza la tassa
pasto_mancia=pasto*mancia

#calcolo della tassa
pasto_tassa=pasto*tassa

#calcolo del pasto compreso mancia e tassa
totale=pasto+pasto_mancia+pasto_tassa

print("l'importo mancia è $%.2f"% pasto_mancia, "l'importo tassa è $%.2f"% pasto_tassa,"il totale è $%.2f"% totale)
