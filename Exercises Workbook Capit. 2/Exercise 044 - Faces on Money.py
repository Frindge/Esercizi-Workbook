# Exercise 44: Faces on Money

# George Washington           $1
# Thomas Jefferson            $2
# Abraham Lincoln             $5
# Alexander Hamilton          $10
# Andrew Jackson              $20
# Ulysses S. Grant            $50
# Benjamin Franklin           $100


money=int(input("Enter the denomination of a banknote: "))

if money ==1:
    dollar="George Washington"
elif money ==2:
    dollar="Thomas Jefferson"
elif money ==5:
    dollar="Abraham Lincoln"
elif money ==10:
    dollar="Alexander Hamilton"
elif money ==20:
    dollar="Andrew Jackson"
elif money ==50:
    dollar="Ulysses S. Grant"
elif money ==100:
    dollar="Benjamin Franklin"
else:
    print("Error, invalid data")
    quit()

print("the denomination of the banknote $%d is %s." % (money, dollar))
