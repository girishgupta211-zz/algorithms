def sort_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1

        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print(arr)


inputs = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],

]
for input_arr in inputs:
    sort_arr(input_arr)
