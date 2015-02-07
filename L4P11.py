def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    lowchar = char.lower()
    #print lowchar
    if lowchar in ['a', 'e', 'i', 'o', 'u']:
    	return True
    else:
    	return False
print isVowel("E")