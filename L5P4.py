def gcdIter(a, b):
	'''
	a, b: positive integers
	
	returns: a positive integer, the greatest common divisor of a & b.
	'''
	loop = min(a, b)
	while loop > 0:
		if a % loop == 0 and b % loop == 0:
			return loop
		else:
			loop -= 1
print gcdIter(17,12)