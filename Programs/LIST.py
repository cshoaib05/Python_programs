a=10
b=20
id(a)			#to check adress
type(a)		#to check data type   							 						#### pooling for integer are done for 256 integer value
	                                        							   				#### if statement work in True and false

print('OUTPUT:',a)		 # , use for printing string with var
print("a=%d b=%d" %(a,b))    # % method of printing
print("a={} b={}".format(a,b))  	 #format method for printing

a=[1,25,36,43,45,46,45,8]  	# create a object of data types
print(a)
print(a[3])		#printing a list

print(len(a))	# length of list
print(min(a))	# min value of list
print(max(a)) 	# max value of list

b=[1,2,'hello','python'] 
print(len(b))

b.insert(3,543) #insert function to insert a value at desire location (index loaction,value)
print(b)		# value shift to next location

b.remove('hello') #remove function to remove the value ( value)
print(b)

print(b.index(2)) #index of (value)

a.sort() # sort a list in assending order object.sort()
print(a)

a.sort(reverse=True)	# to sort a list in decending order
print(a)

a.reverse()  # reverse a list
print(a)

a.clear() 	# clear a list
print(a)

a.append(10) 	# append function to add a var at last fo list
a.append(20)
a.append(30)
a.append(40)
print(a)

a.pop() 	# to remove the last elemnt inserted 
print(a)

a[2]=50		 # to change the element value 
print(a)

c=[[1,2,3],[4,5,6],4,5,a] #multi dimensional list
print(c)
print(c[1][1]) #to print desire index value of d list 


c[4].sort(reverse=True) 
print(c)



							#########    TUPLE     ########

							# Tuple cant be change

d=(1,2,3,6,4)  # defining tuple
print(d)