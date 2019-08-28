# Given a non-negative integer skyline height list, answer how many uninterrupted 1-unit-high horizontal brush strokes are
# needed to cover it.

# https://codegolf.stackexchange.com/questions/179464/covering-a-skyline-with-brush-strokes

# f = lambda A: sum(A) - sum(map(min, A[1:], A))
def f(A):
    right_array = list(A[1:])
    maximum_strokes = sum(A)
    free_strokes = 0
    # if a skyscraper is lower or of equal height as previous skyscraper,
    # then it can be painted freely by using extending previous brushstrokes
    for i in range(len(A) - 1):
        free_strokes = free_strokes + min(A[i], right_array[i])
    minimum_strokes = maximum_strokes - free_strokes
    return minimum_strokes


print(f([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))  # -> 9
print(f([5, 8]))  # -> 8
print(f([1, 1, 1, 1]))  # -> 1
print(f([]))  # -> 0
print(f([0, 0]))  # -> 0
print(f([2]))  # -> 2
print(f([2, 0, 2]))  # -> 4
print(f([10, 9, 8, 9]))  # -> 11
