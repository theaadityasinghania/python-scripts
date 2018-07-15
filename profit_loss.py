cp=int(input("Enter the Cost Price of the product: "))
sp=int(input("Enter the Selling Price of the product: "))
if sp-cp>0:
	print("Profit is: ", sp-cp)
elif cp-sp>0:
	print("Loss is: ",cp-sp)
else:
	print("No Profit, no Loss.")