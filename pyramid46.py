n= int (input("enter number :"))
for i in range(n):
    for j in range(n,i-1):
        if i % 2==0:
            print("#",end="")
        else:
            print(i,end="")
    print()