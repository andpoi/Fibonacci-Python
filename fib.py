#!/usr/bin/python

fib1=0
fib2=1
fib3=0
counter=0
limit=20000

while(counter<limit):
	fib3 = fib1 + fib2
	print fib3
	fib1 = fib2
	fib2 = fib3
	counter+=1
	
print "Done"