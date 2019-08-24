def max_chars(n):
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i] + 1)  # press a
        for j in range(i + 3, min(i + 7, n + 1)):
            dp[j] = max(dp[j], dp[i] * (j - i - 1))  # press select all, copy, paste x (j-i-1)
    return dp[n]


print(max_chars(24))
