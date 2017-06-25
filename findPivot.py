def reverse(arr,start , end):	
	while(start <= end):
		arr[start] , arr[end] = arr[end] , arr[start]
		start = start+1
		end = end-1
	
arr = [1,2 ,3, 4, 5, 6,7, 8, 9]
n = 9
k = 2
reverse(arr,0,n-1)
reverse(arr,0,n-1-k)
reverse(arr,n-k,n-1)

print arr
# [3, 4, 5, 6, 7, 8, 9, 1, 2]
