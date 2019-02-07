import matplotlib.pyplot as plt
x=[10,12,13,17,45,87]
y=['A','B','C','D','E','F']

x1=[15,25,35,45,66,43]
y1=[26,54,23,65,35,64]

plt.hist(x1);
# plt.pie(x,labels=y)
#plt.scatter(x,y,color='black',label='S')
#plt.scatter(x1,y1,color='red',label='T')

plt.title("INFO")
plt.xlabel("STUDENTS")
plt.ylabel("Workshop")
plt.legend()
plt.show()