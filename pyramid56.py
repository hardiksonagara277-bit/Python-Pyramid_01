n = 5

for i in range(n):
    # Print spaces
    print(" " * (n - i - 1), end="")

    # Print characters
    if i == 0:
        print("1")
    elif i == 1:
        print("A B")
    elif i == 2:
        print("a b c")
    elif i == 3:
        print("! ! ! !")
    elif i == 4:
        print('" " " " "')