# Program to check whether a year is leap year or not.



year = int(input("Input a valid year:"))

if year%4==0 and (year%100!=0 or year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")