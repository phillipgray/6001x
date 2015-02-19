def oddTuples(aTup):
	'''
	aTup: a tuple
	
	returns: tuple, every other element of aTup. 
	'''
	newTup = ()
	for i in range(0, len(aTup)):
		#print i #loop checker
		if i % 2 == 0:
			newTup += (aTup[i],)
	return newTup
	#return aTup[0::2] # easiest solution!
b = ('hello', 2, 4, 5.6, 'bones', 'eagleton', 45, 'joe')
print oddTuples(b)