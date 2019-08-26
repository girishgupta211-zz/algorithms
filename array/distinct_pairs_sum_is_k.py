#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. LONG_INTEGER k
#
from collections import defaultdict


def countPairs(arr, targetSum):
    dic = defaultdict(lambda: True)
    pairs = set()
    for elm in arr:
        if (targetSum - elm) in dic:
            pairs.add((elm, targetSum - elm))
        else:
            dic[elm] = True
    return len(pairs)


if __name__ == '__main__':
    print(countPairs([12, 36, 43, 40, 8], 48))
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # arr_count = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(arr_count):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)
    #
    # k = int(input().strip())
    #
    # result = countPairs(arr, k)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
