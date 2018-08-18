import numpy as np
def fillboard(n,m,x,y):
	if(((n*m)-(x+y))%2==0):
		print("YES")
		print(((n*m)-(x+y))//2)
		get_Indexes(n,m,x,y)
	else:
		print("NO")

def valid_index(i,j,n,m,x,y):
	count=0
	for a in range(0,n):
		for b in range(1,m):
			if(a!=i and b!=j):
				count=count+1
				continue
			break
			#print(count)
	if(count>x-1 and count<(n*m-y)):
		return 1
	else:
		return 0

def get_Indexes(n,m,x,y):
	a = np.zeros((n,m))
	print(a)
	value=1
	count=0
	for i in range(0,n):
		for j in range(0,m):
			if(count>x-1 and count<(n*m-y)):
				print(i,j)
				if(a[i,j]==0):
					a[i,j]=value
					if(valid_index(i+1,j,n,m,x,y)==1):
						if(i<n-1 and a[i+1,j]==0):
							a[i+1,j]=value
						else:
							if(valid_index(i,j+1,n,m,x,y)==1):
								if(j<m-1 and a[i,j+1]==0):
									a[i,j+1]=value			

				value=value+1	
			count=count+1
			
	print(a)

fillboard(3,4,1,3)
