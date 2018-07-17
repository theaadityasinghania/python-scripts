for i in range(1,101):
	isPrime=0
	for j in range(2,int(i**1/2)+1):
		if i%j==0:
			isPrime=1
			break
	if isPrime=0:
		print(i)