def get_median(arr, n):
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 - 1]) / 2
    else:
        return arr[n // 2]


def median(arr1, arr2, n):
    if n < 0:
        return -1
    if n == 1:
        return (arr1[0] + arr2[0]) / 2

    if n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

    m1 = get_median(arr1, n)
    m2 = get_median(arr2, n)
    print("median array 1 {}".format(m1))
    print("median array 2 {}".format(m2))
    if m1 > m2:
        if n % 2 == 0:
            return median(arr1[:n // 2], arr2[n // 2:], n // 2)
        else:
            return median(arr1[:n // 2 + 1], arr2[n // 2:], n // 2 + 1)

    if m2 > m1:
        if n % 2 == 0:
            return median(arr2[:n // 2], arr1[n // 2:], n // 2)
        else:
            return median(arr2[:n // 2 + 1], arr1[n // 2:], n // 2 + 1)


ar1 = [8]
ar2 = [2]

ar1 = [1, 12, 15, 26, 38, 40, 67, 87, 89]
ar2 = [2, 13, 17, 30, 45, 56, 86, 109, 110]
# ar2 = [288, 778, 1842, 3035, 3548, 4664, 6729, 6868, 7711, 8723, 8942, 9040,
#        9741, 12316, 12623, 12859, 15006, 15141, 15350, 15890, 17673, 19264,
#        19629, 20037, 22190, 22648, 23805, 24084, 24370, 24393, 25547, 27446,
#        27529, 27644, 28253, 30106, 30333, 31101, 31322, 32662, 32757]
#
# ar1 = [153, 292, 491, 1869, 2995, 3902, 4827, 5436, 5447, 5705, 6334, 9894,
#        9961, 11478, 11538, 11942, 12382, 14604, 14771, 15724, 16827, 17035,
#        17421, 18467, 18716, 19169, 19718, 19895, 19912, 21726, 23281, 23811,
#        24464, 25667, 26299, 26500, 26962, 28145, 28703, 29358, 32391]

len1 = len(ar1)
len2 = len(ar2)
if len1 == len2:
    print("Median is {}".format(median(ar1, ar2, len1)))
else:
    print("No median found")
