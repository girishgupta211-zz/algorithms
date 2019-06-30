# Get number of 1s in binary representation of a number
num = 1025
# num = 1023
ones_count = 0
while num:
    ones_count += (num & 1)
    # Right shift
    num = (num >> 1)
print(ones_count)

# Get number with count in a given array
arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
num_dict = {}
for elm in arr:
    if elm in num_dict.keys():
        num_dict[elm] += 1
    else:
        num_dict[elm] = 1

print(num_dict)

# from collections import Counter
# print(Counter(arr))
