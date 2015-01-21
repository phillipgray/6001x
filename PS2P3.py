balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
lower = balance / 12 
upper = (balance * (1 + monthlyInterestRate) ** 12) / 12
epsilon = 0.01
monthlyPayment = (lower + upper) / 2.0
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
#print "guess: " + str(monthlyPayment)
#print "test: " + str(round(testBal,2))	
while abs(testBal) >= 0.001:
	#print "current monthly payment: " + str(monthlyPayment)
	testBal = balcheck(balance, annualInterestRate, monthlyPayment)
	if testBal > 0.001:
		lower = monthlyPayment
	else:
		upper = monthlyPayment
	monthlyPayment = (lower + upper) / 2.0
#print "Final remaining balance: " + str(round(testBal,2))
print "Lowest payment: " + str(round(monthlyPayment,2))
