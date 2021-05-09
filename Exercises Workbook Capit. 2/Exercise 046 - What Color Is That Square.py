# Exercise 46:What Color Is That Square?

l=input("Enter coordinate letter. ")
num=int(input("Enter coordinate number. "))

y=num % 2
x=num % 2


if l > "h" or num > 8:
    print("Error,beyond letter h and number 8, data not allowed.")
    
elif l=="a" and y==0 or l=="b" and y==1 or l=="b" and y==1 or l=="c" and y==0 \
or l=="d" and y==1 or l=="e" and y==0 or l=="f" and y==1 or l=="g" and y==0 or l=="h" and y==1:
    print ("The box is white.")

else:
    print("The box is black.")



