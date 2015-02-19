def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    totals = 0
    for e in aDict.values():
        for u in e:
            totals += 1
    return totals