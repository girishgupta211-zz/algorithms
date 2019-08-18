def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m - 1, n), lcs(X, Y, m, n - 1))


X = "AGGTAB"
Y = "GXTXAYB"

result = lcs(X, Y, len(X), len(Y))
print(result)

X = "ABCDEFG"
Y = "ABCDFG"

result = lcs(X, Y, len(X), len(Y))
print(result)


def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    dp_arr = [[None] * (n + 1) for i in range(m + 1)]
    print(dp_arr)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_arr[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp_arr[i][j] = 1 + dp_arr[i - 1][j - 1]
            else:
                dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])

    print(dp_arr)
    print(dp_arr[m][n])


X = "ABC"
Y = "AG"
lcs_dp(X, Y)
X = "ABCDEFG"
Y = "ABCDFG"
lcs_dp(X, Y)

X = "AGGTAB"
Y = "GXTXAYB"
lcs_dp(X, Y)
