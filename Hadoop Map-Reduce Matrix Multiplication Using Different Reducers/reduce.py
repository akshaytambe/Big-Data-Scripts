#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

#Importing Libraries
import sys
import string
import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values
arraya = {}
arrayb = {}

#Initialising Variables
s = 0.0
for i in range(0,n):
	arraya[i] = 0.0
	arrayb[i] = 0.0
currentkey = None
printkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key_int, value_int = line.split('\t',1)

	##Parse key/value input - Seperate each field of key/value
	key = key_int.split(" ")
	value = value_int.split(" ")	
	#print '%d %d %s %d %.1f' %(int(key[0]),int(key[1]),value[0],int(value[1]),float(value[2]))

	#Store the Values in Arrays as respect to each Matrix
	if (value[0] == "A"):
		arraya[int(value[1])] = float(value[2])
		#print 'A[%d] = %.1f' %(int(value[1]),float(arraya[value[1]]))

	if (value[0] == "B"):
		arrayb[int(value[1])] = float(value[2])
		#print 'B[%d] = %.1f' %(int(value[1]),float(arrayb[value[1]]))	

	#If we are still on the same key...
	if key_int==currentkey:
		#Process key/value pair
		s = 0.0
		#Matrix Multiplication
		for i in range (0,n):
			s += arraya[i] * arrayb[i]
			
		
	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:
			#compute/output result to STDOUT
			#Print Result
			printkey = currentkey.split(" ")
			print '(%s, %s), %f' %(printkey[0],printkey[1],float(s))

			#Initialise
			for i in range(0,n):
        			arraya[i] = 0.0
        			arrayb[i] = 0.0

			#Restore New Key Value
        		if (value[0] == "A"):
                		arraya[int(value[1])] = float(value[2])
                		#print 'A[%d] = %.1f' %(int(value[1]),float(arraya[value[1]]))

        		if (value[0] == "B"):
                		arrayb[int(value[1])] = float(value[2])
                		#print 'B[%d] = %.1f' %(int(value[1]),float(arrayb[value[1]]))
	
		currentkey = key_int
		#Process input for new key
		s = 0.0

#Compute/output result for the last key
if currentkey == key_int:
	printkey = currentkey.split(" ")
	print '(%s, %s), %f' % (printkey[0],printkey[1], float(s))
