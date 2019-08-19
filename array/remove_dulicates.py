def remove_duplicates_non_sorted(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        j = i + 1
        while j < arr_len:
            if arr[i] == arr[j]:
                left_index = j
                for k in range(left_index, arr_len - 1):
                    arr[k] = arr[k + 1]
                print(arr)
                arr_len = arr_len - 1
            else:
                j += 1
    for l in range(arr_len):
        print(arr[l])


# input_array = [1, 2, 3, 1, 2, 2, 5, 5, 6, 7]
input_array = [1, 2, 3, 1, 2, 2, 5, 5, 6, 7, 1, 2, 7]
remove_duplicates_non_sorted(input_array)


def remove_duplicate_from_sorted_array(arr, n):
    if n == 0 or n == 1:
        return n

    next_unique_index = 0

    for index in range(0, n - 1):
        # Traverse util you find next unique number and increment index
        if arr[index] != arr[index + 1]:
            arr[next_unique_index] = arr[index]
            next_unique_index += 1

    arr[next_unique_index] = arr[n - 1]
    next_unique_index += 1
    for i in range(0, next_unique_index):
        print(arr[i])
    return next_unique_index


input_array = [1, 2, 3, 1, 2, 2, 5, 5, 6, 7, 1]
sorted_array = sorted(input_array)
array_len = len(sorted_array)
res = remove_duplicate_from_sorted_array(sorted_array, array_len)
