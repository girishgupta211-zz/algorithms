"""
Instructions to candidate.
 1) Run this code in the REPL to observe its behaviour. The
    execution entry point is specified at the bottom.
 2) Your task is to implement the following function ('longest_uniform_substring').

     This function should return a tuple that correctly identifies the location
     of the longest uniform substring within the input string.

     e.g.
         - for the input: "abbbccda" the longest uniform substring is "bbb" (which starts at index 1 and is 3 characters long).
         - the tuple returned from the function call would be (1, 3)
 3) If time permits, try to improve your implementation and add more test cases.
"""


def longest_uniform_substring(input):
    if len(input) == 0:
        return (-1, 0)
    next_index = 0
    char_count = 0
    max_count = 1
    new_character = input[0]
    i = 0
    for char in input:
        if char == new_character:
            char_count += 1
        else:
            if char_count > max_count:
                max_count = char_count

                next_index = i
            new_character = char
            char_count = 1
        i += 1

    if next_index == 0:
        return (next_index, char_count)
    else:
        return next_index - max_count, max_count


# char_count = 1
# index = 0
# max_count = 1
# new_character = 0

# todo: implement this function
# return (-1, 0)


def do_tests_pass():
    """Returns True if the test passes. Otherwise returns False."""

    # todo: implement more tests
    test_cases = {
        "": (-1, 0),
        "10000111": (1, 4),
        "aabbbbbCdAA": (2, 5),
        "a": (0, 1)
    }

    passed = True
    for input, result in test_cases.items():
        start, length = longest_uniform_substring(input)
        print(start, length)
        passed = passed and start == result[0] and length == result[1]

    return passed


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass!")
    else:
        print("At least one failure!")