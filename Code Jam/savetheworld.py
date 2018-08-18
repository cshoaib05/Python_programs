


def cal(list):
	
	c=1
	s=1
	damage=0
	for l in list:
		if(l=='C'):
			s=2*s
		else:
			damage+=s
	return damage



def mainn(shelid,a):
	damage=0
	
	#shelid = 6
	c=1
	S=1
	s=1
	count=0
	#a = 'SCCSSC'

	for i in a:

		if 'S'==i:
			damage+=c 
		
		if 'C'==i:
			c=2*c

	else:
		if(damage>shelid):
			a=list(a)
			for q,j in enumerate(a):
				for x,y in enumerate(a):
					if(cal(a)<=shelid):
						return count
					
					if 'S'==y and (x-1)>=0:
						if a[x-1]=='C':
							a[x],a[x-1]='C','S'
							

							count+=1
							break

					if 'C'==j:
					 	S=S*2

			else:
				if(cal(a)<=shelid):
					return count
					


		else:
			return 0
n = int(input())
dnstr = []
for _ in range(n):
	dnstr.append(input())

for i in dnstr:
	shelid = int(i.split(" ")[0])
	a = i.split(" ")[1]

	f=mainn(shelid,a)
	if(f==None):
		print('IMPOSSIBLE')
	else:
		print(f)

# count=mainn()
# print('finalcount',count)


