def find_candidate(arr):
    majority_index = 0
    count = 1

    for i in range(1, len(arr)):
        # print count
        if arr[i] == arr[majority_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            majority_index = i
            count = 1

    return arr[majority_index]


# Function to check if the candidate occurs more than n/2 times
def is_majority(arr, cand):
    count = len(list(filter(lambda x: x == cand, arr)))
    # count = len([x for x in arr if x == cand])
    if count > len(arr) / 2:
        return True
    else:
        return False


input_arr = [3, 3, 3, 3, 3, 5, 2, 2, 2]
candidate = find_candidate(input_arr)

# Print the candidate if it is Majority
if is_majority(input_arr, candidate):
    print("Majority Element: {}".format(candidate))
else:
    print("No Majority Element")
