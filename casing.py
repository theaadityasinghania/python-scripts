# Program to check whether a character is uppercase or lowercase alphabet. Print “U” for uppercase and “L” for lowercase.





a=input("Enter an alphabet: ")
x=ord(a)
if x>=65 and x<=90:
    print("U")
elif x>=97 and x<=122:
    print("L")
else:
    print("S")


# or you can also use
# a=input("Enter an alphabet: ")
# if a>='A' and a<='Z':
#     print("U")
# elif a>='a' and a<='z':
#     print("L")
# else:
#     print("S")