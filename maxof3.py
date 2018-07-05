# Program to find the maximum of three numbers stored in variables.
#Basic approach without using terniary operator or without using any library function.


a=int(input("Enter the first number here: "))
b=int(input("Enter the second number here: "))
c=int(input("Enter the third number here: "))
max=a
if b>max:
    max=b
if c>max:
    max=c
print ("The greatest number is: ",max)