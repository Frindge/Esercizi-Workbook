# Exercise 43: Frequency to Note 

# C4   261.63
# D4   293.66
# E4   329.63
# F4   349.23
# G4   392.00
# A4   440.00
# B4   493.88

Freq=float(input("Enter the Frequency: "))

if Freq >260.62 and Freq <262.64:
    print("C4")
elif Freq >292.65 and Freq < 294.67:
    print("D4")
elif Freq >329.62 and Freq <331.64:
    print("E4")
elif Freq >348.22 and Freq <350.24:
    print("F4")
elif Freq >391.99 and Freq <393.01:
    print("G4")
elif Freq >439.00 and Freq <441.00:
    print("A4")
elif Freq >492.87 and Freq <494.89:
    print("B4")
else:
    print("Error,invalid data")
