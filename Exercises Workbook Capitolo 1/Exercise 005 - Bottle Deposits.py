# In molte giurisdizioni viene aggiunto un piccolo deposito sui contenitori di bevande per incoraggiare le persone
# a riciclarli.In una particolare giurisdizione, i contenitori per bevande da un litro o meno hanno un deposito
# di 0,10 dollari e i contenitori per bevande da più di un litro hanno un deposito di 0,25 dollari.

# Scrivi un programma che legga il numero di contenitori di ogni dimensione dall'utente. Il tuo programma dovrebbe
# continuare calcolando e visualizzando il rimborso che sarà ricevuto per la restituzione di quei contenitori.
# Formattate l'output in modo che includa il segno del dollaro e due cifre a destra del punto decimale.


# deposito in dollari fino a 1 litro
deposito1=(0.10)
# deposito in dollari oltre 1 litro
deposito2=(0.25)

contenitori1=int(input("Quanti contenitori fino a 1 litro vuoi consegnare? "))
contenitori2=int(input("quanti contenitori oltre 1 litro vuoi consegnare? "))

rimborso=(contenitori1*deposito1+contenitori2*deposito2)

print("il rimborso è di $%.2f" %rimborso)



