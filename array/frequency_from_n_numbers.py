# find frequency of all numbers from an array ranging numbers from 1 to n
arr = [3, 2, 6, 1, 5, 6, 5, 2, 3]
arr = [elm - 1 for elm in arr]
n = len(arr)
for i, num in enumerate(arr):
    arr[arr[i] % n] = arr[arr[i] % n] + n

for i, num in enumerate(arr):
    print("{} : {}".format(i + 1, num // n))
