def isMatch(string, pattern):
    """
    :type string: str
    :type pattern: str
    :rtype: bool
    """

    # Using DP
    #
    string_len = len(string)
    pattern_len = len(pattern)
    lookup = [[False for _ in range(pattern_len + 1)] for _ in range(string_len + 1)]
    lookup[0][0] = True

    # Only '*' can match with empty string
    for j in range(1, pattern_len + 1):
        if pattern[j - 1] == '*':
            lookup[0][j] = lookup[0][j - 1]

    for i in range(1, string_len + 1):
        for j in range(1, pattern_len + 1):
            #  Two cases if we see a '*'
            #       a) We ignore ‘*’ character and move to next  character in the pattern,
            #                  i.e., ‘*’ indicates an empty sequence.
            #       b) '*' character matches with previous character in input
            if pattern[j - 1] == '*':
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]

            #  Current characters are considered as
            #              matching in two cases
            #              (a) current character of pattern is '?'
            #              (b) characters actually match
            elif pattern[j - 1] == string[i - 1] or pattern[j - 1] == '?':
                lookup[i][j] = lookup[i - 1][j - 1]

            # If characters don't match
            elif pattern[j - 1] != string[i - 1]:
                lookup[i][j] = False

    return lookup[string_len][pattern_len]


# A function to run test_me cases
def test_me(first, second):
    if isMatch(first, second):
        print("Yes")
    else:
        print("No")


# Driver program
test_me("", "**", )  # Yes
test_me("geeks", "g*ks", )  # Yes
test_me("geeksforgeeks", "ge?ks*", )  # Yes
test_me("gee", "g*k")  # No because 'k' is not in second
test_me("abcd", "abc*c?d", )  # No because second must have 2 instances of 'c'
test_me("abcd", "*c*d", )  # Yes
test_me("abcd", "*?c*d")  # Yes
