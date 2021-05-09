# Exercise 40: Sound Levels

# Jackhammer 130 dB
# Gas Lawnmower 106 dB
# Alarm Clock 70 dB
# Quiet Room 40 dB

Sound=float(input("Enter a number to define a sound level in decibels: "))

if Sound > 130:
    Sound="The sound level is louder than a Jackhammer"
elif Sound == 130:
    Sound="The sound level is Jackhammer" 
elif Sound > 106 :
    Sound="The sound level is between Gas Lawnmower and Jackhammer"
elif Sound == 106:
    Sound="The sound level is Gas Lawnmower"
elif Sound > 70 :
    Sound="The sound level is between Alarm Clock and Gas Lawnmower"
elif Sound == 70:
    Sound="The sound level is Alarm Clock"
elif Sound >40 :
    Sound="The sound level is between Quiet Room and Alarm Clock"
elif Sound == 40:
    Sound="The sound level is Quiet Room"
else:
    Sound="The sound leve is between silence and Quiet Room"

print(Sound)
