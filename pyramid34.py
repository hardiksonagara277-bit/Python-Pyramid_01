n=int(input("enter number :"))
for i in range(n):
    print('  ' * i, end='')
    for j in range(5 - i):
        print(9 - 2*j - 2*i, end='')
    print()