list1=[10,202,30,44,430]
maximum=0
minimum=0
list1.sort()
print(list1)
for i in range(1,5):
	maximum=list1[i]+maximum

for j in range(0,4):
	minimum=list1[j]+minimum
	
print(maximum,minimum)

