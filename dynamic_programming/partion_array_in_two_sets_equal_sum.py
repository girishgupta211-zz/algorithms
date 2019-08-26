# Dynamic Programming based python program to partition problem
# Returns true if arr[] can be  partitioned in two subsets of
# equal sum_required, otherwise false
import functools


def can_partition(num):
    s = sum(num)
    # if 's' is a an odd number, we can't have two subsets with equal sum_required
    if s % 2 != 0:
        return False

    return can_partition_recursive(num, s / 2, 0)


def can_partition_recursive(num, sum_required, current_index):
    # base check
    if sum_required == 0:
        return True

    n = len(num)
    if n == 0 or current_index >= n:
        return False

    # recursive call after choosing the number at the `current_index`
    # if the number at `current_index` exceeds the sum_required, we shouldn't process this
    if num[current_index] <= sum_required:
        if can_partition_recursive(num, sum_required - num[current_index], current_index + 1):
            return True

    # recursive call after excluding the number at the 'current_index'
    return can_partition_recursive(num, sum_required, current_index + 1)


print("Can partition: " + str(can_partition([1, 2, 3, 4])))
print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
print("Can partition: " + str(can_partition([2, 3, 4, 6])))


# formula -> Matrix[i][j] = matrix[i-1][j-array[j]]
# result :--> last row and last column
def findPartition(arr, n):
    # calculate sum_required of all elements
    sum = functools.reduce(lambda a, b: a + b, arr)
    # if sum_required is odd then it can not be partitioned.
    if sum % 2 != 0:
        return False
    # Rows will have array numbers and column will represent sum_required
    lookup = [[None for _ in range(sum // 2 + 1)] for _ in range(n + 1)]

    # initialize leftmost column as True. as zero sum_required can be achieved by any number
    for i in range(0, n + 1):
        lookup[i][0] = True

    # initialize top row as False as without using any elements no sum_required can be made except [0,0]
    for j in range(1, sum // 2 + 1):
        lookup[0][j] = False

    # fill the partition table in  bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum // 2 + 1):
            # if we can get the sum_required 'j' without the number at index 'i'
            if lookup[i - 1][j]:
                lookup[i][j] = lookup[i - 1][j]
            # else if we can find a subset to get the remaining sum_required
            elif j >= arr[i - 1]:
                lookup[i][j] = lookup[i - 1][j - arr[i - 1]]

    return lookup[n][sum // 2]


# Driver Code
arr = [3, 1, 5, 7]
n = len(arr)
if findPartition(arr, n):
    print("Can be divided into two subsets of equal sum_required")
else:
    print("Can not be divided into two subsets of equal sum_required")

print("Can partition: " + str(findPartition([1, 2, 3, 4], 4)))
print("Can partition: " + str(findPartition([1, 1, 3, 4, 7], 5)))
print("Can partition: " + str(findPartition([2, 3, 4, 6], 4)))
