symbols = ["\\", ":", "~", "|", "/"]

for i in range(len(symbols)):
    for j in range(i + 1):
        print(symbols[i], end="")
    print()