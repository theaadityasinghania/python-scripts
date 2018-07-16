n=int(input("Eneter a number: "))
fac=1
for i in range(n,0,-1):
	fac*=i
print("The factorial of the given number is: ",fac)