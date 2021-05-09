# Exercise 31: Units of Pressure

# Libbre per pollice quadrato
psi = 0.145038  
# atmosfere
atm = 0.00986923  
# millimetri di mercurio
mmHg = 7.5006

KPa=float(input("iserisci un valore in kilopascal: "))

a=KPa * psi
b=KPa * atm
c=KPa * mmHg

print("""la conversione da kilopascal in Libbre per pollice quadrato è:%.2f
in atmosfere è:%.2f
in millimetri di mercurio è:%.2f""" % (a, b, c))
