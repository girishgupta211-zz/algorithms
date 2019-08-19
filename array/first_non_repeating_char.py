# Non-Repeating Element
from collections import Counter
from collections import defaultdict


# Method 1
def first_non_repeating_char(input_arr):
    counter = Counter(input_arr)
    for elem in counter:
        if counter[elem] == 1:
            return elem
    return "No element found"


arr = [9, 4, 9, 6, 7, 4, 6]
status = first_non_repeating_char(arr)
print(status)


# Method 2
def first_non_repeating_char(input_arr):
    char_dict = defaultdict(lambda: 0)
    for elm in input_arr:
        char_dict[elm] += 1

    for elem in char_dict:
        if char_dict[elem] == 1:
            return elem
    return "No element found"


arr = [9, 4, 9, 6, 7, 4, 6, 7]
status = first_non_repeating_char(arr)
print(status)


# Method 3
def first_non_repeating_char(input_arr):
    arr_len = len(input_arr)
    for i, elem in enumerate(input_arr):
        j = 0
        while j < arr_len:
            if elem == input_arr[j] and i != j:
                break
            j += 1

        if j == arr_len:
            return input_arr[i]


arr = [9, 4, 9, 6, 8, 4, 6]
status = first_non_repeating_char(arr)
print(status)
