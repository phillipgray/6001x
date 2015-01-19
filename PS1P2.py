s = "adbaehoboboobobasdlfajbob"
counter = 0
ind = 0
for i in s:
	if s[ind:(ind+3)] == "bob":
		counter += 1
	ind += 1
print "Number of times bob occurs is: " + str(counter)