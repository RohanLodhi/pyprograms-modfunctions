from sys import *

for i in argv:
	print(i)
	

print("Path: ",path)

var = stdin.readline()
print("Input: ",var)

a = 10.36
print("Size of Float: ",getsizeof(a))

a = 10
print("Size of: Int",getsizeof(a))
print("Type is: ",type(a))

a = 4+5j
print("Size of: Complex ",getsizeof(a))

a = ""
print("Size of: String",getsizeof(a))

