# L'area di un triangolo può essere calcolata usando la seguente formula, dove b è la lunghezza della base del
# triangolo e h è la sua altezza: b*h/2
# Scrivi un programma che permetta all'utente di inserire i valori di b e h. Il programma dovrebbe poi calcolare
# e visualizzare l'area di un triangolo con base di lunghezza b e altezza h.


b=float(input("Inserire un valore numerico da dare alla base: "))
h=float(input("Inserire un valore numerico da dare all'altezza: "))
#formula dell'area del triangolo
area=(b*h)/2

print("l'area del triangolo è:", area)
