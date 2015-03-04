def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string

    #important variables
    keepPlayingTrigger = True
    livesNumber = 2
    availableLetters = string.ascii_lowercase
    lettersGuessedList = []

    #game beginning sequence
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %s letters long." % (str(len(secretWord)))

    #main game sequence
    while keepPlayingTrigger == True:
        print "-------------"
        print "You have %s guesses left." % (livesNumber)
        availableLetters = getAvailableLetters(lettersGuessedList)
        print "Available letters: %s" % (availableLetters) 
        currentLetter = raw_input("Please guess a letter: ")
        if currentLetter in lettersGuessedList:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessedList)
            continue

        lettersGuessedList.append(currentLetter)

        if lettersGuessedList[-1] not in secretWord:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessedList)
            livesNumber -= 1

        if lettersGuessedList[-1] in secretWord:
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessedList)
                
        keepPlayingTrigger = not isWordGuessed(secretWord, lettersGuessedList) and livesNumber != 0
    

    # end of game: two options: 1) out of guesses and 2) you guessed the word
    else:
        print "-------------"
        # print livesNumber
        if livesNumber == 0:
            print "Sorry, you ran out of guesses. The word was %s." % (secretWord)
        elif isWordGuessed(secretWord, lettersGuessedList):
            print "Congratulations, you won!"