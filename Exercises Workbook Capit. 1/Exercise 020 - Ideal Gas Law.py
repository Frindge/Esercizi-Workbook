# La legge dei gas ideali è un'approssimazione matematica del comportamento dei gas al variare di pressione,
# volume e temperatura. Di solito viene enunciata come:
# PV=nRT 
# dove P è la pressione in Pascal, V è il volume in litri, n è la quantità di sostanza in moli, R è la costante
# dei gas ideali, pari a 8.314 J /(mol k) e T è la temperatura in gradi Kelvin. 

# Scrivi un programma che calcoli la quantità di gas in moli quando l'utente fornisce la pressione, il volume e la
# temperatura. Prova il tuo programma determinando il numero di moli di gas in una bombola SCUBA. Una tipica
# bombola SCUBA contiene 12 litri di gas ad una pressione di 20.000.000 Pascal (circa 3.000 PSI). La temperatura
# ambiente è di circa 20 gradi Celsius o 68 gradi Fahrenheit.

# Suggerimento: una temperatura viene convertita da Celsius a Kelvin aggiungendovi 273,15.
# Per convertire una temperatura da Fahrenheit a Kelvin, detrarre 32 da essa, moltiplicare per 5/9


P=float(input("inserisci la quantità di Pressione: "))
V=float(input("inserisci la quantità di Volume: "))
T_Celsius=float(input("inserisci la Temperatura in Celsius: "))
# R è la costante dei gas ideali
R=8314
# da Celsius a Kelvin
T_kelvin=T_Celsius + 273.15
# formula per trovare quantità di sostanza in moli
n_moli=(P*V) / (R*T_kelvin)

print("La quantità di gas in moli è %.2f:" % n_moli)
