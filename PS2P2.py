#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
monthCounter = 0
monthlyInterestRate = annualInterestRate / 12.0
minMonthlyPayment = 0.0
monthlyUnpaidBalance = 0.0
totalMonthlyPayment = 0.0
oldBal = balance
newBal = 0.0
while monthCounter in range(0,12):
	monthCounter += 1
	print "Month: " + str(monthCounter)
	minMonthlyPayment = oldBal * monthlyPaymentRate
	totalMonthlyPayment += minMonthlyPayment
	print "Minimum monthly payment: " + str(round(minMonthlyPayment,2))
	monthlyUnpaidBalance = oldBal - minMonthlyPayment
	newBal= monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
	print "Remaining balance: " + str(round(newBal,2))
	oldBal = newBal
print "Total paid: " + str(round(totalMonthlyPayment,2))
print "Remaining balance: " + str(round(oldBal,2))