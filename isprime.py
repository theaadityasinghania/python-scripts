n=int(input("Enter a number here: "))
isPrime=0
for i in range(2,int(n**1/2)+1):
	if n%i==0:
		isPrime=1
		break
if isPrime==0:
	print("Given number is Prime.")
else:
	print("Given number is not Prime.")