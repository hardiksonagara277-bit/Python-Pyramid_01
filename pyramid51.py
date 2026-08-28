n = int (input("enter number:"))
for i in range (n,0,-1):
    for j in range (n-i):
        print(" ",end="")
    for k in range (1,i+1):
        if i % 2== 0:
            print("*",end=" ")
        else:
            print("*",end=" ")
    print()
for l in range (n+1):
    for m in range (n-l):
        print(" ",end="")
    for o in range (1,l+1):
        if l % 2== 0:
            print("*",end=" ")
        else:
            print("*",end=" ")
    print()