def sort_arr(arr):
    left, mid = [0] * 2
    right = len(arr) - 1
    while mid <= right:
        # Increment left index while we see 0 at left
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[right], arr[mid] = arr[mid], arr[right]
            right -= 1

    print(arr)


inputs = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 0, 1, 2, 2],
    [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
]
for input_arr in inputs:
    sort_arr(input_arr)
