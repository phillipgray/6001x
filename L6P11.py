def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    #keylist = aDict.keys()
    if aDict == {}:
        return None
    else:
        valueSum = []
        for e in aDict.values():
            valueSum.append(len(e))
        #print "valueSum check: " #the next three lines are value checks for debugging
        #print valueSum
        #print "max valueSum check: " + str(max(valueSum))
        winner = valueSum.index(max(valueSum)) #this crazy nested thing takes the max element count from valueSum and returns the index of that element in valueSum
        #print "winner check: " + str(winner) # another value check
        return aDict.keys()[winner] #returns the indexed key (by winner) of original aDict
#animals = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon', 'buzzard', 'bunny'], 'd': ['donkey', 'dog', 'dingo']}
#print biggest(animals)
#test1 = {'a': [3, 12, 7, 16, 9, 5, 4, 15, 4, 19], 'c': [19, 13, 20, 16, 9, 13], 'b': [12], 'd': [9, 4, 17, 11, 18, 12, 9, 9]}
#print biggest(test1)
#test2 = {'Y': []}
#print biggest(test2)