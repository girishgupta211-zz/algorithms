def wordBreak(words_dict, string):
    if len(string) == 0:
        return True
    i = 1
    while i < len(string):
        # consider all prefixes of current string
        prefix = string[0:i]
        # return true if prefix is present in the dictionary and remaining
        # string also forms space-separated sequence of one or more dictionary words

        if prefix in words_dict and wordBreak(words_dict, string[i:]):
            return True
        i += 1

        # return false if the string can't be segmented
    return False


dict = ["this", "th", "is", "famous", "Word", "break", "b", "r", "e", "a", "k", "br", "bre", "brea", "ak", "problem"]
str = "Wordbreakproblem"
if (wordBreak(dict, str)):
    print("String can be segmented")
else:
    print("String can't be segmented")
