def binSearch(arr,beg,end,key):
	mid = beg + (end - beg)/2
	if(beg > end):
		return -1
	if(arr[mid] == key):
		return mid
	elif (key < arr[mid]):
		return binSearch(arr,beg,mid-1,key)
	else:
		return binSearch(arr,mid+1,end,key)




arr = [1,2,3,4,5,6,7,8,9]
beg = 0
end = len(arr) -1
mid = beg + (end - beg)/2
key = 9
print binSearch(arr,beg,end,key)
