def count(arr, m, sum):
    if sum == 0:
        return 1

    if sum < 0:
        return 0

    if m <= 0 and sum >= 1:
        return 0

    return count(arr, m, sum - arr[m - 1]) + count(arr, m - 1, sum)


arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))

arr = [1, 2, 3, 5, 6]
m = len(arr)
print(count(arr, m, 10))
