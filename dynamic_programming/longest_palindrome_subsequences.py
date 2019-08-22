def lps(arr, i, n):
    # Base Case 1: If there is only 1 character
    if i == n:
        return 1

    # Base Case 2: If there are only 2 characters and both are same
    elif i + 1 == n and arr[i] == arr[n]:
        return 2

    # If the first and last characters match
    elif arr[i] == arr[n]:
        return 2 + lps(arr, i + 1, n - 1)

    # If the first and last characters do not match
    else:
        return max(lps(arr, i + 1, n), lps(arr, i, n - 1))


X = "GEEKSFORGEEKS"
result = lps(X, 0, len(X) - 1)
print(result)


def lps_dp(arr, n):
    dp_arr = [[0 for j in range(n)] for j in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # If this is diagonal element
            if i == j:
                dp_arr[i][j] = 1

            # if there are only 2 elements
            elif i + 1 == j and arr[i] == arr[j]:
                dp_arr[i][j] = 2

            # if elements are same then add 2 to left bottom cell
            elif arr[i] == arr[j]:
                dp_arr[i][j] = 2 + dp_arr[i + 1][j - 1]

            # take maximum of next row same column and same row previous column
            else:
                dp_arr[i][j] = max(dp_arr[i + 1][j], dp_arr[i][j - 1])

    # return first row last column
    return dp_arr[0][n - 1]


X = "GEEKSFORGEEKS"
result = lps_dp(X, len(X))
print(result)
