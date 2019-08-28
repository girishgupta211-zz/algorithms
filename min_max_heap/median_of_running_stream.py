# Given that integers are being read from a data stream. Find median of all the elements read so far starting
# from the first integer till the last integer. The data stream can be any source of data,
# example: a file, an array of integers etc

import heapq


def addNum(num, lowers, highers):
    # if this is first number then add to max_heap
    # if new number is less than maximum of max_heap then add to max_heap
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers, -num)

    # if new number is more than minimum of min_heap then add to min_heap
    else:
        heapq.heappush(highers, num)


def rebalance(lowers, highers):
    # if elements in max_heap if more than in min_heap, then pop from max_heap and push to min_heap
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers, -heapq.heappop(lowers))
    # if elements in min_heap if more than in max_heap, then pop from min_heap and push to max_heap
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers, -heapq.heappop(highers))


def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0]) / 2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])


def runningMedian(a):
    lowers = []  # max heap, vals should go in and come out negated
    highers = []  # min heap, vals should go in positive
    result = []
    for v in a:
        addNum(v, lowers, highers)
        rebalance(lowers, highers)
        result.append(round(getMedian(lowers, highers), 1))
    return result


print(runningMedian([100, 1, 23, 4, 4, 5, 19, 102]))
