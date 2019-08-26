def isMatch(string, pattern):
    """
    :type string: str
    :type pattern: str
    :rtype: bool
    """

    # Using DP
    #
    m = len(string)
    n = len(pattern)
    lookup = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    lookup[0][0] = True
    #    Only '*' can match with empty string
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            lookup[0][j] = lookup[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #  Two cases if we see a '*'
            #              a) We ignore ‘*’ character and move
            #                 to next  character in the pattern,
            #                  i.e., ‘*’ indicates an empty sequence.
            #              b) '*' character matches with ith
            #                  character in input 
            if pattern[j - 1] == string[i - 1] or pattern[j - 1] == '?':
                lookup[i][j] = lookup[i - 1][j - 1]

            #  Current characters are considered as
            #              matching in two cases
            #              (a) current character of pattern is '?'
            #              (b) characters actually match
            elif pattern[j - 1] == '*':
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]
            # If characters don't match
            else:
                lookup[i][j] = False

    return lookup[m][n]


# A function to run test cases
def test(first, second):
    if isMatch(first, second):
        print("Yes")
    else:
        print("No")


# Driver program
test("geeks", "g*ks", )  # Yes
test("geeksforgeeks", "ge?ks*", )  # Yes
test("gee", "g*k")  # No because 'k' is not in second
test("abcd", "abc*c?d", )  # No because second must have 2 instances of 'c'
test("abcd", "*c*d", )  # Yes
test("abcd", "*?c*d")  # Yes
