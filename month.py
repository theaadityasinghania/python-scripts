# Program which takes month number and print number of days in that month.
# For example:
# For month=1 print “31 days”
# For month=2 print “28 days”






x=int(input("Enter a month here: "))
if x>=1 and x<=12:
    if x==2:
        print("28 Days")
    elif x<8:
        if x%2==0:
            print("30 Days")
        else:
            print("31 Days")
    else:
        if x%2==0:
            print("31 days")
        else:
            print("30 days")
else:
    print("Enter a valid month")