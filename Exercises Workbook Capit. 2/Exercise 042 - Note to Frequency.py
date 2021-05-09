# Exercise 42: Note to Frequency

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

note = str(input("Enter a note: "))
note=note.title()
octave = int(input("Enter octave: "))
if note == "C":
    Freq = C4
    frequency = Freq / 2 ** (4 - octave)
elif note == "D":
    Freq = D4
    frequency = Freq / 2 ** (4 - octave)
elif note == "E":
    Freq = E4
    frequency = Freq / 2 ** (4 - octave)
elif note == "F":
    Freq = F4
    frequency = Freq / 2 ** (4 - octave)
elif note == "G":
    Freq = G4
    frequency = Freq / 2 ** (4 - octave)
elif note == "A":
    Freq = A4
    frequency = Freq / 2 ** (4 - octave)
elif note == "B":
    Freq = B4
    frequency = Freq / 2 ** (4 - octave)
else:
    print("invalid data")
    quit()
    
print("The %s have %.2f frequency" % (note, frequency))

