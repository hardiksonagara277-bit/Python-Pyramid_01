n = int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(1,i):
        print(" ", end="")
    for k in range(i,n+1):
        print(k, end=" ")
    print()