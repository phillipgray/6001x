def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    if s1 == "":
    	return s2
    elif s2 == "":
    	return s1
    else:
	    laced = ""
	    index = 0
	    diff = abs(len(s1)-len(s2))
	    def shortstr(s1, s2):
	    	if len(s1) > len(s2):
	    		return s2
	    	else:
	    		return s1
	    def longstr(s1, s2):
	    	if len(s1) > len(s2):
	    		return s1
	    	else:
	    		return s2
	    for char in shortstr(s1, s2):
	    	laced += s1[index]
	    	laced += s2[index]
	    	index += 1
	    left = longstr(s1, s2)
	    print left
	    laced += left[index:(index + diff)]
	    return laced
a = 'hello'
b = 'hello'
c = laceStrings(a, b)
print c