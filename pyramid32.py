n = int (input("enter number :"))
for i in range(n+1):
    print(' ' * i, end='')
    for j in range(5 - i):
        print(9 - 2*j, end='')
    print()
