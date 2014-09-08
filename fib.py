#!/usr/bin/python

fib1=0
fib2=1
fib3=0
limit=90000000000000000000000000000000000000000000000000000000000000000000000000

while(fib3<limit):
	fib3 = fib1 + fib2
	print fib3
	fib1 = fib2
	fib2 = fib3
	
print "Done"