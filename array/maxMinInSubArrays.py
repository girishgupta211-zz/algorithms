INT_MIN = -10000000


def maxMinInSubarrays(a, m):
    n = len(a)
    max_of_min = INT_MIN
    for i in range(n - m + 1):
        minimum = a[i]
        for j in range(m):
            if a[i + j] < minimum:
                minimum = a[i + j]
        if minimum > max_of_min:
            max_of_min = minimum
    return max_of_min


arr = [2, 5, 4, 6, 8]
maxMinInSubarrays(arr, 3)
