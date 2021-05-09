# Scrivi un programma che chieda all'utente di inserire la larghezza
# e la lunghezza di una stanza. Una volta letti questi valori, il vostro
# programma dovrebbe calcolare e visualizzare l'area della stanza.
# La lunghezza e la larghezza saranno inserite come numeri in virgola mobile.
# Includi le unità di misura nel tuo prompt e nel messaggio di output;
# piedi o metri, a seconda dell'unità con cui ti trovi più a tuo agio a lavorare.


larghezza=float(input("Inserisci la lunghezza della tua stanza in metri: "))
lunghezza=float(input("Inserisci la larghezza della tua stanza in metri: "))

area=larghezza*lunghezza

print("l'area della stanza è di ", area,"metri")

