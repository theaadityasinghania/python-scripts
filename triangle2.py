x=int(input("Enter first side of the triangle: "))
y=int(input("Enter second side of the triangle: "))
z=int(input("Enter third side of the triangle: "))

if x+y<z or y+z<x or z+x<y:
	print("This triangle cannot be formed.")
else:
	if x==y && y==z:
		print("Equilateral trianle.")
	elif x==y or y==z or z==x:
		print("Isoceles triangle.")
	else:
		print("Scalene triangle.")