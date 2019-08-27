"""
Python3 program to merge k sorted arrays of size n each
"""
import sys
from typing import List
import heapq

Matrix = List[List[int]]


def merge_k_sorted_arrays(arr: Matrix):
    min_heap = []
    result_size = 0
    for i in range(len(arr)):
        # first element is array value,
        # second element is array index ,
        # third is index of next element to be picked from array
        heapq.heappush(min_heap, (arr[i][0], [i, 1]))
        result_size += len(arr[i])

    result = [0] * result_size
    for i in range(result_size):
        # take the minimum
        root = heapq.heappop(min_heap)
        heap_element = root[0]
        arr_index = root[1][0]
        next_elm_idx = root[1][1]
        result[i] = heap_element
        # Find the next element that will replace current root of heap.
        # The next element belongs to same array as the current root.
        if next_elm_idx < len(arr[arr_index]):
            value = arr[arr_index][next_elm_idx]
            heapq.heappush(min_heap, (value, [arr_index, next_elm_idx + 1]))
        else:
            heapq.heappush(min_heap, (sys.maxsize, []))
    print(*result)


if __name__ == '__main__':
    arr = [
        [2, 6, 12, 34],
        [1, 9, 20],
        [23, 34, 90, 2000],
        [-1],
        [0]
    ]
    print('Merged Array is:')
    merge_k_sorted_arrays(arr)
