s = "abcddeibyehfvabcdefg0"
longest = ""
lesslong = ""
startindex = 0
index = 0
endindex = 1
for char in s:
	print s[index]+s[endindex]
	if s[index] < s[endindex]:
		index += 1
		endindex += 1
	elif s[index] >= s[endindex]: #index is 3, endindex is 4, startindex is 0
		lesslong = s[startindex:endindex] # this will give s[0:4]
		print "this is the current string evaluated: " + lesslong
		if len(lesslong) > len(longest): # testing to find the longest string
			longest = lesslong #storing longest string
		print "this is the current longest string: " + longest
		startindex = endindex # updates slice starting point
		index += 1
		endindex += 1
print longest