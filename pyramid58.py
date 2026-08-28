rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(i):
        print(i + j, end=" ")
    for j in range(i - 2, -1, -1):
        print(i + j, end=" ")
    print()