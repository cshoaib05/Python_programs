value1 = 1
value2 = 10
l=[]
count=0
for x in range(1,100):
	l.append(x*x)

for x in range(value1,value2+1):
	if x*x in l:
		count=count+1

print(count)