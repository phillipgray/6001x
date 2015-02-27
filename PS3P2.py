def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWordList = []
    for char in secretWord:
        if char in secretWordList:
            pass
        else:
            secretWordList.append(char)
    #print secretWordList
    for i in secretWordList:
        if i not in lettersGuessed:
            #print i + " not in letters guessed"
            return False
        else:
            #print i + " in letters guessed"
            pass
    return True