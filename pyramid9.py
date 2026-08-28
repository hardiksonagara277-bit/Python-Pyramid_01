n=int(input("enter number "))
for i in range(1,n+1):
    num = i * 2 - 1 
    for j in range(i):
        print(num ,end="")
    print()