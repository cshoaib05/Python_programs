from operator import add

def zeropad(s):
	while (len(s)<4):
		s.insert(0,'0')
	return s

def comp(c):
	for i in range(0,len(c)):
		if(c[i]=='0'):
			c[i]=1
		if(c[i]=='1'):
			c[i]=0
	print(c)
	b=[0,0,0,1]
	d=add(c,b)
	return d

def add(c,b):


	
a=int(input("ENter 1st no:"))
b=int(input("ENter 1st no:"))

s1=bin(a)
s2=bin(b)

l1=list(s1)[2:]
l1=list(s1)[2:]

m=zeropad(l1)
q=zeropad(l2)

print(m)
print(q)

mc=comp(m)
print(mc)
