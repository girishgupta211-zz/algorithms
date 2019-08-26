# Dynamic Programming based python program to partition problem
# Returns true if arr[] can be  partitioned in two subsets of
# equal sum, otherwise false
import functools


# A recursive Python3 program for
# partition problem

# A utility function that returns
# true if there is a subset of
# arr[] with sun equal to given sum
def isSubsetSum(arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # If last element is greater than sum, then
    # ignore it
    if arr[n - 1] > sum:
        return isSubsetSum(arr, n - 1, sum)

    ''' else, check if sum can be obtained by any of 
    the following 
    (a) including the last element 
    (b) excluding the last element'''

    return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])


# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
def findPartion(arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % 2 != 0:
        return False

    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum(arr, n, sum // 2)


# Driver program to test above function
arr = [3, 1, 5, 9, 12]
n = len(arr)
if findPartion(arr, n) :
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")


# This code is contributed by shreyanshi_arun.

def findPartition(arr, n):
    # calculate sum of all elements
    sum = functools.reduce(lambda a, b: a + b, arr)
    if sum % 2 != 0:
        return False

    lookup = [[True for _ in range(n + 1)] for _ in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        lookup[0][i] = True

    # initialize leftmost column, except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        lookup[i][0] = False

    # fill the partition table in  bottom up manner
    for i in range(1, sum // 2 + 1):
        for j in range(1, n + 1):
            lookup[i][j] = lookup[i - arr[j - 1]][j - 1]

    return lookup[sum // 2][n]


# Driver Code
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
if findPartition(arr, n):
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")
