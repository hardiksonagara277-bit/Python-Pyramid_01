n=int(input("enter number:"))
for i in range(n+1):
    for j in range(1,(i+1)):
        if i % 2 == 0:
            print("0",end="")
        else:
            print("1",end="")
    print()
	