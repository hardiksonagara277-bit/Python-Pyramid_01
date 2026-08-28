
# 1#3#5
# 1#3#
# 1#3
# 1#
# 1

n= 5

for i in range(n , 0 , -1):
	for j in range(1, i + 1):
		if j % 2 == 0:
			print("#", end="")
		else:
			print(j, end = "")
	print()