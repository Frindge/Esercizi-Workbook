# Creare un programma che legga due numeri interi, a e b, dall'utente. Il vostro programma dovrebbe calcolare e
# visualizzare:

# -La somma di a e b
# -La differenza quando b viene sottratto da a
# -Il prodotto di a e b
# -Il quoziente quando a è diviso per b
# -Il resto quando a è diviso per b
# -Il risultato di log10 a
# -Il risultato di a elevato a potenza b  (a**b)

# Suggerimento: probabilmente troverete utile la funzione log10 nel modulo math
# per calcolare il penultimo elemento della lista.

from math import log10

a=int(input("Inserisci un numero intero da impostare ad a: "))
b=int(input("Inserisci un numero intero da impostare ad b: "))

print("\nLa somma di a+b è:",a+b)
print("La differenza di a-b è:",a-b)
print("Il prodotto di a*b è:" ,a*b)
print("Il della divisione di a/b è:", a/b)
print("Il resto quando a è diviso per b è:", a%b)
print("Il risultato di log10 a è:", log10(a))
print("Il risultato di a elevato a potenza b è:", a**b)
