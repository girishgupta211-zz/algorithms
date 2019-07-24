from collections import OrderedDict


def find_lexographical_subsequence(input_str, start, end, final_result=""):
    print(input_str)
    if start == end:
        return final_result

    first_char = input_str[start]
    ordered = OrderedDict()
    for index in range(start, end):
        ordered[input_str[index]] = True

    result = ''.join([item for item in ordered])

    if first_char < result[0]:
        result.replace(first_char, '')
        result = first_char + result

    # final_result = final_result + result
    # todo remove already exiting first_char if present

    return find_lexographical_subsequence(input_str, start + 1, end, result)


# 'cabc'
# 'cab'

input_str = 'cacbdacb'
result = ""
find_lexographical_subsequence(input_str, 0, len(input_str), result)
