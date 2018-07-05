# Program to print the minimum number of Rupee notes needed to match a given amount. Available denominations of notes are 2000, 500, 100, 50.
# For example, if the amount is 28,550, then you need 14 notes of 2000, 1 note of 500, and 1 note of 50. So total number of notes is 14+1+1 = 16.





x=int(input("Enter an amount here: "))
count=0
count+=x//2000
x=x%2000
count += x // 500
x = x % 500
count += x // 100
x = x % 100
count += x // 50
x = x % 50
print(count)