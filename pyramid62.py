rows = 3
num = 1

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i):
        print(f"{num**3:<5}", end=" ")
        num += 1
    print()