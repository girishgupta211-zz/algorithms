# Get number of 1s in binary representation of a number
a = 1023
count = 0
while a:
    count = count + (a & 1)
    # Right shift
    a = (a >> 1)
print(count)

# Get number with count in a given array
arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
num_dict = {}
for elm in arr:
    if elm in num_dict.keys():
        num_dict[elm] += 1
    else:
        num_dict[elm] = 1

print(num_dict)
