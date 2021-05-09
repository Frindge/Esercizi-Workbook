# Exercise 33: Sort 3 Integers

# Creare un programma che legga tre numeri interi dall'utente e li mostri in ordine ordinato
# (dal più piccolo al più grande). Usate le funzioni min e max per trovare il valore più piccolo e
# quello più grande. Il valore medio può essere trovato calcolando la somma di tutti e tre i valori,
# e poi sottraendo il valore minimo e quello massimo.


a=int(input("inserisci il primo numero intero: "))
b=int(input("inserisci il secondo numero intero: "))
c=int(input("inserisci il terzo numero intero: \n"))

d=min(a, b, c)
f=max(a, b, c)
e=(a+b+c-d-f)

print("il numero più piccolo è:",d)
print("il numero intermedio è:",e)
print("il numero maggiore è:",f)
