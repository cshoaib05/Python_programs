def kangaroo(x1,v1,x2,v2):
	if(x1<x2 and v1<v2):
		print("NO")
		return 0 
	if(x1>x2):
		print("NO")
		return 0
	if(x1==x2):
		print("YES")
		return 0
	kangaroo(x1+v1,v1,x2+v2,v2)

kangaroo(0,3,4,2)