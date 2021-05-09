# Exercise 62: Roulette Payouts

# green 0 and 00
# red 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36.
# Single number (1 to 36, 0, or 00)
# Red versus Black
# Odd versus Even (Note that 0 and 00 do not pay out for even)
# 1 to 18 versus 19 to 36



from random import randint
rand_num=randint(0, 38)
# rand_num=int(input("numero "))

if rand_num == 37:
    single_number = "00"
elif rand_num == 0:
    single_number = "0"
    print("The spin resulted in %s ..." % single_number)
    print("Pay %s" % single_number)
else:
    if (
        (rand_num % 2 == 1 and rand_num >= 1 and rand_num <= 9)
        or (rand_num % 2 == 0 and rand_num >= 12 and rand_num <= 18)
        or (rand_num % 2 == 1 and rand_num >= 19 and rand_num <= 27)
        or (rand_num % 2 == 0 and rand_num >= 30 and rand_num <= 36)
    ):
        color = "Red"
    else:
        color = "Black"
    if rand_num % 2 == 1:
        odd_vs_even = "Odd"
    else:
        odd_vs_even = "Even"
    if rand_num >= 1 and rand_num <= 18:
        range_numb = "1 to 18"
    else:
        range_numb = "19 to 36"
    print("The spin resulted in %i ..." % rand_num)
    print("Pay %i" % rand_num)
    print("Pay %s" % color)
    print("Pay %s" % odd_vs_even)
    print("Pay %s" % range_numb)
