def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWordList = []
    guessedWordList = []

    for char in secretWord:
        secretWordList.append(char)
    #print secretWordList
    for i in secretWordList:
        if i not in lettersGuessed:
            #print i + " not in letters guessed"
            guessedWordList.append("_ ")
        else:
            #print i + " in letters guessed"
            guessedWordList.append(i + " ") 
    #print guessedWordList
    currentGuessedWord = "".join(guessedWordList)
    #print currentGuessedWord
    return currentGuessedWord