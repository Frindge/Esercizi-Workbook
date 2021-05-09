# Exercise 57: Cell Phone Bill 

# telephone rate 50 min and 50sms in $15 to month
# $0.25 for min additional
# $0.15 for sms additional
# $0.44 cost additional to month to support 911
# telephone rate 5% tax including $0.44 support to 911

# write the program

# min and sms to month     fact
# rate base to month       fact
# min additional           fact
# sms additional           fact
# support to 911           fact
# tax                      fact
# total cost   all in .2f  fact

phone_rate=15
min_additional=0.25
sms_additional=0.15
support_911=0.44
tax=0.05


minutes=float(input("enter the amount of minutes used: "))
sms=int(input("enter the amount of sms used: "))
print()

# calculation of basic tariff 15 + support and tax 5%
rate_base_to_month=((phone_rate+support_911)*tax)+(phone_rate+support_911)


if minutes >50:
    minutes=(minutes-50)*min_additional
elif minutes <=50:
    minutes=(minutes-minutes)
 
if sms > 50:
    sms=(sms-50)*sms_additional
elif sms <=50:
    sms=(sms-sms)

total_tax=((phone_rate+support_911+ sms + minutes)*tax)
total=phone_rate+support_911+ sms + minutes+total_tax

print("basic rate per month with 50 minutes and 50 sms including tax and 911 support is $:%.2f " % rate_base_to_month)
print("additional minutes $%.2f after the 50th minute the cost is $:%.2f"% (min_additional, minutes))
print("additional sms $%.2f after the 50th sms the cost is $:%.2f"% (sms_additional, sms))
print("the cost of 911 support is $0.44 per month")
print("the tax is %.2f per month, this month's tax is $%.2f" % (tax, total_tax))
print("total cost is:$%.2f" % total)



