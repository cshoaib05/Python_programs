import math
a=10
b=20

abs(-20) 		#convert negative into positive
print(math.fabs(-20)) 	#it convert only for int
print(math.ceil(20.5)) 		# it round fgure the value to most
print(math.floor(20.5))        # it round figure the value to least
print(math.log(9))    # log
print(math.log10(9))  # log10
pow(10,2)  # power(number,power)
print(math.sqrt(5)) # square root 

											###### STRING ###############

s='hello world'

																		### end in python is -1
print(s[2])
print(s[2:8])
print(s[2:8:2])

print(s.upper()) # upper letter
print(s.lower()) # lower letter
print(s.capitalize()) #capitalize first letter
print(s.split())   # split the string using parameter pass ( to split with var)
print(s.find('e')) # to find location

s1="SHOAIB"
s2=".C"

print(s1+s2)  # adding the string
print(s*20)

print('S' in s1) # to find 

print(s1 is s2) # to compare
