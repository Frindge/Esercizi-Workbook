# Exercise 35: Even or Odd?

number=int(input("Enter a valid integer number: "))
number1=number % 2

if number1 == 0:
    number1="the number is even."
else:
    number1="the number is odd: "

print(number1)
