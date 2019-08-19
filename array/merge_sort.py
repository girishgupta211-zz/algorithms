def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


assert merge([1, 4, 6, 9], [3, 5, 7, 8, 10, 11]) == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]

result = merge_sort([1, 6, 9, 4, 5, 7, 3, 10, 8, 11])
print(result)
