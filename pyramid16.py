n=int(input("enter number "))
for i in range(n):
    for j in range(i,n):
        print(2*(n-j)-1,end="")
    print()