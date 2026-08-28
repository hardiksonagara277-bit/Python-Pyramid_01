n=int(input("enter number :"))
for i in range (n,0,-1):
    num = i*2-1
    for j in range(i):
        print(num,end="")
    print()
