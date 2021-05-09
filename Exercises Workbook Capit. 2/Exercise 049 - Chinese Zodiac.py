#Exercise 49: Chinese Zodiac

# 2000          Dragon
# 2001          Snake
# 2002          Horse 
# 2003          Sheep
# 2004          Monkey
# 2005          Rooster
# 2006          Dog
# 2007          Pig
# 2008          Rat
# 2009          Ox
# 2010          Tiger
# 2011          Hare


years=int(input("Enter the year to be checked: "))

if years % 12 == 0:
    sign = "Monkey"
elif years % 12 == 1:
    sign = "Rooster"
elif years % 12 == 2:
    sign = "Dog"
elif years % 12 == 3:
    sign = "Pig"
elif years % 12 == 4:
    sign = "Rat"
elif years % 12 == 5:
    sign = "Ox"
elif years % 12 == 6:
    sign = "Tiger"
elif years % 12 == 7:
    sign = "Hare"
elif years % 12 == 8:
    sign = "Dragon"
elif years % 12 == 9:
    sign = "Snake"
elif years % 12 == 10:
    sign = "Horse"
elif years % 12 == 11:
    sign = "Sheep"
print(sign)
