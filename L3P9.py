upper = 100
lower = 0
guess = 50
option = ""
print "Please think of a number between 0 and 100!"
while option != "c":
	print "Is your secret number " + str(guess) + "?"
	option = raw_input("Enter 'h' to indicate the guess is too high. " +
		"Enter 'l' to indicate the guess is too low. Enter 'c' to indicate " +
		"I guessed correctly ")
	if option == "h":
		upper = guess
		guess = (lower + upper)/ 2
	elif option == "l":
		lower = guess
		guess = (lower + upper)/ 2
	elif option == "c":
		print "Game over. Your secret number was: " + str(guess)
	else:
		print "Sorry, I did not understand your input."