from sys import maxint
arr = [3,3,3,3,3,5,2,2,2]
majority_index = 0
count = 1

for i in range(1,len(arr)):	
	# print count
	if(arr[i] == arr[majority_index]):
		count+=1
	else:
		count-=1
	
	if(count == 0):
		majority_index = i
		count = 1
	# print arr[majority_index]


print(arr[majority_index])


