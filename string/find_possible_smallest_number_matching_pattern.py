# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/amp/
# Form minimum number from given sequence


def find_possible_smallest_number_matching_pattern(pattern):
    n = len(pattern)
    if n >= 9:
        return "-1"

    if not ('I' in pattern or 'D' in pattern):
        return "-1"

    result = ""
    stk = []
    for i in range(0, n + 1):
        stk.append(i + 1)

        if i == n or pattern[i] == 'I':
            while stk:
                result += str(stk.pop())
    return result


inputs = ["IDID", "I", "DD", "II",
          "DIDI", "IIDDD", "DDIDDIID", "IIIIIIIIII", "MNNNM"]

for Input in inputs:
    print(*(find_possible_smallest_number_matching_pattern(Input)))
