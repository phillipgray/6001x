def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans = 1
    if exp == 0:
    	return ans
    else:
    	while exp > 0:
    		ans = base * ans
    		exp -= 1
    		#print "loop # " + str(exp)
    		#print "current ans: " + str(ans)
    	return ans
#print iterPower(5,3)