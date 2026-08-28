rows = 5

for i in range(1, rows + 1):
    if i % 2 == 1:      
        ch = "$"
    else:        
        ch = "@"
    for j in range(i):
        print(ch, end=" ")
    print()