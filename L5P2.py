def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
    	return 1
    elif exp == 1:
    	return base
    else:
    	#print "loop # " + str(exp)
    	return base * iterPower(base, exp - 1)
#print iterPower(5,3)