# Exercise 36: Dog Years

# first 2 human years in dog years
Y_dog=2*10.5
# for every human years after first 2
Y_dog3=4

Y_human=float(input("Enter years: "))

if Y_human == 1:
    Dog=Y_dog/2
elif Y_human == 2:
    Dog=Y_dog

if Y_human >2:
    Dog1=(Y_human-2)*4
    Dog=Y_dog+Dog1
else:
    print("invalid data ")
    quit()

print(Dog)
