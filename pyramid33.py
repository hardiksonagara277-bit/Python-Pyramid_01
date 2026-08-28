n = int(input("enter number :"))
for i in range(n):
    print(' ' * i, end="")
    for j in range(i, 5):
        print(1 + 2*j, end='')
    print()
