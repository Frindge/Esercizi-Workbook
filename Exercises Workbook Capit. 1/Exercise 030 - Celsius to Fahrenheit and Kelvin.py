# Exercise 30: Celsius to Fahrenheit and Kelvin


Celsius=float(input("inserisci un valore di temperatura in gradi Celsius: "))

Celsius_a_Fahreneit= Celsius * (9/5) + 32

Celsius_a_Kelvin= Celsius + 273.15

print("La conversione da Celsius è: %.2f kelvin, %.2f Fahreneit " % (Celsius_a_Kelvin, Celsius_a_Fahreneit))
