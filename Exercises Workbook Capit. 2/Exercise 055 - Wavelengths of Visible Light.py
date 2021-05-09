# Exercise 55:Wavelengths of Visible Light 

# Violet            380 to less than 450
# Blue              450 to less than 495
# Green             495 to less than 570
# Yellow            570 to less than 590
# Orange            590 to less than 620
# Red               620 to 750

wavelength=float(input("Enter a wavelength: "))

if wavelength >=380 and wavelength <450:
    print("The wavelength is Violet")
elif wavelength >=450 and wavelength < 495:
    print("The wavelength is Blue")
elif wavelength >= 495 and wavelength < 570:
    print("The wavelength is Green")
elif wavelength >= 570 and wavelength < 590:
    print("The wavelength is Yellow")
elif wavelength >= 590 and wavelength < 620:
    print("The wavelength is Orange")
elif wavelength >= 620 and wavelength < 750:
    print("The wavelength is Red")
else:
    print("invalid data, min 380 max 750")
