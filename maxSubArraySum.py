from sys import maxint
arr = [-2, -3, 4, -1, -2, 1, 5, -3 ]
# arr = [-13, -3, -25, -20, -3, -16, 23, -12, -5, 22, -15, -4, -7]

maxSofar = -maxint - 1
currMax = 0
for item in arr:	
	currMax = currMax + item
	if( currMax  > maxSofar ):
		maxSofar = currMax
	if(currMax < 0):
		currMax = 0
	# print currMax
	# print maxSofar

print maxSofar	
# print currMax