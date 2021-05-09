# Exercise 50: Richter Scale

# Meno di 2,0                                 Micro
# Da 2,0 a meno di 3,0                        Very Minor
# Da 3,0 a meno di 4,0                        Minor
# Da 4,0 a meno di 5,0                        Light
# Da 5,0 a meno di 6,0                        Moderate
# Da 6,0 a meno di 7,0                        Strong
# Da 7,0 a meno di 8,0                        Major
# Da 8,0 a meno di 10,0                       Great
# 10.0 o più                                  Meteoric

Magnitude=float(input("Enter the Magnitude in this mode - 2.5: "))

if Magnitude <2.0:
    a="Micro"
elif Magnitude <3.0:
    a="Minor"
elif Magnitude <4.0:
    a="Very Minor"
elif Magnitude <5.0:
    a="Light"
elif Magnitude <6.0:
    a="Moderate"
elif Magnitude <7.0:
    a="Strong"
elif Magnitude <8.0:
    a="Major"
elif Magnitude <10.0:
    a="Great"
else: 
    a="Meteoric"

print("a magnitude %.1f earthquake is considered to be a %s earthquake." % (Magnitude, a))
