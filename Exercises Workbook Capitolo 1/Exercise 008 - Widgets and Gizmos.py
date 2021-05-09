# Un rivenditore online vende due prodotti: widgets e gizmos. Ogni widget pesa 75 grammi. Ogni gizmo pesa 112 grammi.
# Scrivi un programma che legga il numero di widget e il numero di gizmo dall'utente. Poi il tuo programma dovrebbe
# calcolare e visualizzare il peso totale dei pezzi.

widgets_grammi=75
gizmo_grammi=112

widget=int(input("Quanti widget vuoi? "))
gizmo=int(input("Quanti gizmo vuoi? "))

kilogrammi=0.001 # 1 kilogrammo in grammi

# peso totale dei pezzi
peso_totale=(widget*widgets_grammi+gizmo*gizmo_grammi)

# stampa in grammi
print("il peso totale in grammi sono:", peso_totale)

#stampa in kilogrammi
print("il peso totale in kilogrammi sono:", peso_totale*kilogrammi)
