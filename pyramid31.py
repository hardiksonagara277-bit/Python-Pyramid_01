n= int(input("enter number :"))
for i in range(n,0,-1):
	for j in range(2*i-1,0,-2):
		print(j, end = "")
	print()