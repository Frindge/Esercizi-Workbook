# Fate finta di aver appena aperto un nuovo conto di risparmio che guadagna il 4% di interessi all'anno.
# L'interesse che si guadagna viene pagato alla fine dell'anno e viene aggiunto al saldo del conto di risparmio.
# Scrivete un programma che inizi leggendo l'importo del denaro depositato sul conto dall'utente. Poi il programma
# dovrebbe calcolare e visualizzare l'importo nel conto di risparmio dopo 1, 2 e 3 anni. Visualizzate ogni importo
# in modo che sia arrotondato a 2 cifre decimali.


# interesse per ogni fine anno
int_annuo=4/100  #4%

deposito=float(input("Inserire l'importo da depositare: "))
print("\nIl tuo deposito attuale è di: $",deposito)

deposito2=(deposito*int_annuo) # interesse 4% del primo anno

importo1=deposito+deposito2 # importo del primo anno + l'interesse
print("\nIl primo anno ha generato un'interesse di $%.2f" % deposito2,
      "\nil totale nel tuo conto è di $:%.2f" % importo1)

interesse2=importo1*int_annuo # interesse 4% del secondo anno

importo2=importo1+interesse2 # importo del secondo anno + l'interesse
print("\nIl secondo anno ha generato un'interesse di $%.2f" % interesse2,
      "\nil totale nel tuo conto è di $:%.2f" % importo2)

interesse3=importo2*int_annuo # interesse 4% del secondo anno

importo3=importo2+interesse3 # importo del secondo anno + l'interesse
print("\nIl terzo anno ha generato un'interesse di $%.2f" % interesse3,
      "\nil totale nel tuo conto è di $:%.2f" % importo3)
