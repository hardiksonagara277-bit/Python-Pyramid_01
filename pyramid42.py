n=int(input("enter number :"))
for i in range (n,0,-1):
    num = i*1
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(num,end=" ")
    print()
