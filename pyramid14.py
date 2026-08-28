n= int (input("enter number :"))

for i in range (n,0,-1):
    for j in range(i):
        print(9-2*j,end="")
    print()