arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170,171,172,173,174,175,176]
elm = 10
k = 0
while (True):
	try:
		i = 2**k - 1 # 0, 1, 3, 7, 15
		# print k
		if(arr[i] == elm):
			print "found at " + str(i)
			exit()
		elif( arr[i] > elm):
			break					
	
	except Exception as e:			
		break
	k = k+1
			
begin = 2**(k-1)
end = 2**k -1

while (begin <= end):
	mid = begin + (end-begin)/2	
	try:
		if(arr[mid] == elm):
			print "found at " + str(mid)
			exit()			
		elif(arr[mid] < elm):
			begin = mid+1		
		else:
			end = mid-1

	except Exception as e:
		end = mid-1

print "Element not found"

