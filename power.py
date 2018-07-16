a=int(input("Enter a number: "))
b=int(input("Enter the power to raise: "))
pow=1
for i in range(b):
	pow*=a
print(pow)