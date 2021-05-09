# Exercise 56: Frequency to Name

frequency=float(input("Enter the radiation frequency: "))

if frequency >= 3 * 10**19:
    name ="Gamma Rays"
elif frequency >= 3 * 10**17:
    name ="X-Rays"
elif frequency >= 7.5 * 10**14:
    name ="Ultraviolet Light"
elif frequency >= 4.3 * 10**14:
    name ="Visible Light"
elif frequency >= 3 * 10**12:
    name ="Infrared Light"
elif frequency >= 3 * 10**9:
    name ="Microwaves"
else:
    nome ="Radio Waves"

print("the entered frequency corresponds to %s" % name)
