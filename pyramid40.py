n = int (input("enter number :"))
for i in range(n):
    print(' ' * i, end='')
    for j in range(n, i, -1):
        print(j , end=' ')
    print()
