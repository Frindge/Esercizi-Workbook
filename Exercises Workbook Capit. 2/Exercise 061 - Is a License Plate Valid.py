# Exercise 61: Is a License Plate Valid?

plate=input("Enter the license plate: ")
plate=plate.upper()

if len(plate) < 6 or len(plate) > 7:
    print("Error, invalid data")
elif len(plate) == 6 and \
plate[0] >= "A" and plate[0] <= "Z" and \
plate[1] >= "A" and plate[1] <= "Z" and \
plate[2] >= "A" and plate[2] <= "Z" and \
plate[3] >= "0" and plate[3] <= "9" and \
plate[4] >= "0" and plate[4] <= "9" and \
plate[5] >= "0" and plate[5] <= "9":
    plate=plate
    


elif len(plate) == 7 and \
plate[0] >= "0" and plate[0] <= "9" and \
plate[1] >= "0" and plate[1] <= "9" and \
plate[2] >= "0" and plate[2] <= "9" and \
plate[3] >= "0" and plate[2] <= "9" and \
plate[4] >= "A" and plate[2] <= "Z" and \
plate[5] >= "A" and plate[2] <= "Z" and \
plate[6] >= "A" and plate[2] <= "Z":
    plate=plate
    
if len(plate) == 6:
    print("The plate %s is a valid older style plate" % plate)
else:
    print("The plate %s is a valid new style plate" % plate)
