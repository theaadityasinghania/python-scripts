# Program that prints “YES” if a number is divisible by both 5 and 11, and prints “NO” otherwise.



x=int(input("Enter a number here:"))
if x%5==0 and x%11==0:
    print("YES")
else:
    print("NO")