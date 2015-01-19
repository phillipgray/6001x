s = "abcddeijkbyehfvabcdefg"
s = s + "0"
longest = ""
lesslong = ""
startindex = 0
index = 0
endindex = 1
for char in s[:-1]:
	if s[index] <= s[endindex]:
		index += 1
		endindex += 1
	elif s[index] > s[endindex]: #index is 3, endindex is 4, startindex is 0
		lesslong = s[startindex:endindex] # this will give s[0:4]
		if len(lesslong) > len(longest): # testing to find the longest string
			longest = lesslong #storing longest string
		startindex = endindex # updates slice starting point
		index += 1
		endindex += 1
print "Longest substring in alphabetical order is: " + longest