# Exercise 34: Day Old Bread
# Una panetteria vende pagnotte di pane a 3,49 dollari l'una. Il pane vecchio di un giorno è scontato del 60%.
# Scrivi un programma che inizi leggendo il numero di pagnotte di pane vecchio di un giorno acquistate dall'utente.
# Poi il vostro programma dovrebbe visualizzare il prezzo regolare del pane, lo sconto perché è vecchio di un giorno,
# e il prezzo totale. Ognuno di questi importi dovrebbe essere visualizzato sulla propria linea con un'etichetta
# appropriata. Tutti i valori dovrebbero essere visualizzati usando due cifre decimali, e i punti decimali in
# tutti i numeri dovrebbero essere allineati quando l'utente inserisce valori ragionevoli.


# prezzo regolare
pagnotta=3.49
# sconto del 60%
giorno=0.6

pane_vecchio=int(input("inserisci la quantità di pane vecchio acquistate: "))

p_regolare=pane_vecchio * pagnotta

p_scontato=p_regolare * giorno

p_finale=p_regolare - p_scontato

print("\nprezzo regolare: %.2f" % p_regolare)
print("prezzo scontato: %.2f" % p_scontato)
print("prezzo finale  : %.2f" % p_finale)
