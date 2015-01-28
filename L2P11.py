varA = raw_input("What's the first variable?")
varB = raw_input("What's the second variable?")
if type(varA) == str: 
    print "string involved"
elif type(varB) == str:
    print "string involved"
elif varA == varB:
    print "equal"
elif varA > varB:
    print "bigger"
elif varA < varB:
    print "smaller"