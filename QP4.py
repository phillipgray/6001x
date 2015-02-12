def myLog(x, b):
	'''
	x: a positive integer
	b: a positive integer; b >= 2

	returns: log_b(x), or, the logarithm of x relative to a base b
	'''
	ans = 0
	while b ** ans <= x:
		#print "trying " + str(ans)
		if b ** (ans + 1) > x:
			break
		else:	
			ans += 1
	return ans
#print myLog(15, 3)
#print myLog(16, 2)
