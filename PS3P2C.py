def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    leftoverLettersList = []
    for char in string.ascii_lowercase:
        # print char
        if char not in lettersGuessed:
            # print "added %s" % (char)
            leftoverLettersList.append(char)
        # print leftoverLettersList
    leftoverLetters = "".join(leftoverLettersList)
    return leftoverLetters