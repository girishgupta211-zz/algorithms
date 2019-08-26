# Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
# C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in
# individual strings is preserved ~~~~Asked in : Yahoo, Yatra


def is_interleaved(array1, array2, string):
    if len(array1) + len(array2) != len(string):
        return False

    M = len(array1)
    N = len(array2)
    dp_arr = [[False] * (N + 1) for i in range((M + 1))]

    dp_arr[0][0] = True

    # If If string1 is empty
    for j in range(1, N + 1):
        dp_arr[0][j] = dp_arr[0][j - 1] and array2[j - 1] == string[j - 1]

    # If If string2 is empty
    for i in range(1, M + 1):
        dp_arr[i][0] = dp_arr[i - 1][0] and array1[i - 1] == string[i - 1]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if array1[i - 1] == string[i + j - 1]:
                dp_arr[i][j] = dp_arr[i - 1][j]

            elif array2[j - 1] == string[i + j - 1]:
                dp_arr[i][j] = dp_arr[i][j - 1]

            else:
                dp_arr[i][j] = False

    # print(dp_arr)
    return dp_arr[M][N]


print(is_interleaved('ABC', 'DEF', 'ADEBCF'))
print(is_interleaved('ab', 'cdef', 'bacdef'))
print(is_interleaved('ab', 'cdef', 'abcdef'))
print(is_interleaved('ab', 'cdef', 'cdefab'))
print(is_interleaved('XXY', 'XXZ', 'XXZXXXY'))
