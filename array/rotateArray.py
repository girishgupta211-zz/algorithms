def reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# Rotate an array by k elements
input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 9
k = 2
reverse(input_arr, 0, n - 1)
reverse(input_arr, 0, n - 1 - k)
reverse(input_arr, n - k, n - 1)

print(input_arr)
# [3, 4, 5, 6, 7, 8, 9, 1, 2]
