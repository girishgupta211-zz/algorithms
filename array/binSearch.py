def binary_search(arr, beg, end, search_key):
    mid = beg + (end - beg) // 2
    if beg > end:
        return -1
    if arr[mid] == search_key:
        return mid
    elif search_key < arr[mid]:
        return binary_search(arr, beg, mid - 1, search_key)
    else:
        return binary_search(arr, mid + 1, end, search_key)


input_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
key = 40
found_index = binary_search(input_arr, 0, len(input_arr) - 1, key)
if found_index == -1:
    print("Key: {} does not exist in array:".format(key))
else:
    print("Key: {} found at index [{}]:".format(key, found_index))
