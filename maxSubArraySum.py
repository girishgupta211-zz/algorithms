import sys

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# arr = [-13, -3, -25, -20, -3, -16, 23, -12, -5, 22, -15, -4, -7]
max_so_far = -sys.maxsize - 1
currMax = 0
for item in arr:
    currMax = currMax + item
    if currMax > max_so_far:
        max_so_far = currMax
    if currMax < 0:
        currMax = 0
# print currMax
# print maxSofar

print(max_so_far)
# print currMax
