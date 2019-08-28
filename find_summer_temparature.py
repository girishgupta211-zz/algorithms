# I've just tried a coding challenge to write a function that returns the length of the shortest possible
# left partition of an array of numbers, all of whose elements are less than all of the elements in the corresponding right partition.
#
# The scenario given was finding the divide between "winter" and "summer" given a variable number of monthly
# temperature readings, with the rule that all winter temperatures are lower than all summer temperatures.
# We can assume that there is at least one correct partition, and the goal is to get the shortest winter.
# https://stackoverflow.com/questions/46689119/finding-array-partition-where-maxleft-minright-possible-in-on-time
def solution(arr):
    left_max = maximum = arr[0]
    position = 1  # there is always one day of winter

    for i in range(1, len(arr) - 1):
        if arr[i] < left_max:
            position = i + 1
            left_max = maximum
        elif arr[i] > maximum:
            maximum = arr[i]
    return position


print(solution([5, -2, 3, 8, 6]))
print(solution([-5, -5, -5, -42, 6, 12]))


def shortestWinterLength(arr):
    if len(arr) == 0:
        return 0

    winter_high = arr[0]
    overall_high = arr[0]
    winter_length = 0

    # Get max in the left array
    for temperature in arr:
        if temperature <= winter_high:
            winter_high = overall_high
        elif temperature > overall_high:
            overall_high = temperature

    # count all the values which are less than max in left array
    for temperature in arr:
        if temperature <= winter_high:
            winter_length += 1

    # total length of the left array
    return winter_length


print(shortestWinterLength([5, -2, 3, 8, 6]))
print(shortestWinterLength([-5, -5, -5, -42, 6, 12]))
