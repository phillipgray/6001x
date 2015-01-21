balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 10
monthlyUnpaidBalance = 0.0
testBal = 1.0
def balcheck(balance, annualInterestRate, monthlyPayment):
	"""
	This function takes a balance (float), annual interest rate (float),
	and monthlyPayment (float) and calculates the remaining
	balance after 12 monthly payments.
	"""
	oldBal = balance
	for i in range(1,13):
		monthlyUnpaidBalance = oldBal - monthlyPayment
		newBal= monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
		oldBal = newBal
	return newBal
	
testBal = balcheck(balance, annualInterestRate, monthlyPayment)
#print "test: " + str(round(testBal,2))	
while testBal > 0:
	#print "current test balance: " + str(testBal)
	testBal = balcheck(balance, annualInterestRate, monthlyPayment)
	if testBal > 0:
		monthlyPayment += 10
#print "Final remaining balance: " + str(round(testBal,2))
print "Lowest payment: " + str(monthlyPayment)
