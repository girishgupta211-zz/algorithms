# we have a specially made keyboard which has following four keys 1.
# This key prints character 'A' 2. (Ctrl-A) 3. (Ctrl-C) 4. (Ctrl-V)
# If you are allowed to press keys of this special keyboard N times,
# write a program which calculates maximum numbers of A's possible ~~~~Asked in : Google, Adobe, NetApp

def max_key_strokes(n):
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i] + 1)  # press a
        for j in range(i + 3, min(i + 7, n + 1)):
            dp[j] = max(dp[j], dp[i] * (j - i - 1))  # press select all, copy, paste x (j-i-1)
    return dp[n]


print(max_key_strokes(24))
print(max_key_strokes(6))
