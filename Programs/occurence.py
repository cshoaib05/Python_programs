k=0
print('ENTER THE ELEMENTS')
l=[int(input()) for i in range(0,5)]
for m  in l:
	for n in l:
		print(m,n)
		if(m==n):
			print(m,n)
			k+1
			if(k==2):
				print(m)
				break
