# we have a specially made keyboard which has following four keys 1.
# This key prints character 'A' 2. (Ctrl-A) 3. (Ctrl-C) 4. (Ctrl-V)
# If you are allowed to press keys of this special keyboard N times,
# write a program which calculates maximum numbers of A's possible ~~~~Asked in : Google, Adobe, NetApp


def max_key_strokes(n):
    lookup = [0] * (n + 1)
    for i in range(n):
        lookup[i + 1] = max(lookup[i + 1], lookup[i] + 1)  # press a
        for j in range(i + 3, min(i + 7, n + 1)):
            lookup[j] = max(lookup[j], lookup[i] * (j - i - 1))  # press select all, copy, paste x (j-i-1)
    return lookup[n]


print(max_key_strokes(24))
print(max_key_strokes(6))


def find_max_key_strokes(n):
    if n <= 6:
        return n

    max_so_far = 0
    for b in range(n - 3, 0, -1):
        curr = (n - b - 1) * find_max_key_strokes(b)
        max_so_far = max(max_so_far, curr)

    return max_so_far


print(find_max_key_strokes(24))
print(find_max_key_strokes(6))


def maxA(N):
    best = [0, 1, 2, 3, 4, 5, 6, 9, 12,
            16, 20, 27, 36, 48, 64, 81]
    q = (N - 11) // 5 if N > 15 else 0
    return best[N - 5 * q] * 4 ** q


print(maxA(24))
print(maxA(6))
