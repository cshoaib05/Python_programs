no=6
for x in range(1,no):
	for y in range(1,x+1):
		print(str(y),end='')
		if (y<x):
			print(" ",end='')
	if(x!=no-1):
		print("\\n")