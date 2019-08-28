import random


class BinaryHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get(self, i):
        return self.items[i]

    def get_max(self):
        if self.size() == 0:
            return None
        else:
            return self.items[0]

    def get_min(self):
        if self.size() == 0:
            return None
        else:
            return self.items[0]

    def extract_max(self):
        if self.size() == 0:
            return None

        maximum = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return maximum

    def extract_min(self):
        if self.size() == 0:
            return None
        minimum = self.get_min()
        # put last element from heap in the front
        self.items[0] = self.items[-1]
        # delete the last node
        del self.items[-1]
        # heapify it again
        self.min_heapify(0)
        return minimum

    # This is in place changes for array, so return is not required
    def max_heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        if left < self.size() and self.get(left) > self.get(index):
            maximum = left
        else:
            maximum = index
        if right < self.size() and self.get(right) > self.get(maximum):
            maximum = right
        if maximum != index:
            self.items[maximum], self.items[index] = self.items[index], \
                                                     self.items[maximum]
            self.max_heapify(maximum)

    def min_heapify(self, index):
        # percolate down in heap
        # start from top till bottom
        left = self.left(index)
        right = self.right(index)
        if left < self.size() and self.get(left) < self.get(index):
            minimum = left
        else:
            minimum = index
        if right < self.size() and self.get(right) < self.get(minimum):
            minimum = right
        if minimum != index:
            self.items[minimum], self.items[index] = self.items[index], \
                                                     self.items[minimum]
            self.min_heapify(minimum)

    def insert_max_heap(self, key):
        # percolate up in heap in Array
        index = self.size()
        self.items.append(key)

        while index != 0:
            parent_index = self.parent(index)
            if self.get(parent_index) < self.get(index):
                self.items[index], self.items[parent_index] = \
                    self.items[parent_index], self.items[index]
            index = parent_index

    def insert_min_heap(self, key):
        index = self.size()
        self.items.append(key)

        while index != 0:
            parent_index = self.parent(index)
            if self.get(parent_index) > self.get(index):
                self.items[index], self.items[parent_index] = \
                    self.items[parent_index], self.items[index]
            index = parent_index


if __name__ == '__main__':
    max_heap1 = BinaryHeap()
    max_heap1.insert_max_heap(12)
    max_heap1.insert_max_heap(31)
    max_heap1.insert_max_heap(11)
    max_heap1.insert_max_heap(123)
    max_heap1.insert_max_heap(43)
    max_heap1.insert_max_heap(67)
    max_heap1.insert_max_heap(78)
    print("max heap1")
    while max_heap1.size() != 1:
        print(max_heap1.extract_max())

    max_heap2 = BinaryHeap()
    total = 0
    print("max heap2")
    while total < 10:
        max_heap2.insert_max_heap(random.randint(1000, 2000))
        total += 1

    while max_heap2.size() != 1:
        print(max_heap2.extract_max())

    min_heap = BinaryHeap()
    total = 0
    print("min heap1")
    while total < 10:
        min_heap.insert_min_heap(random.randint(1000, 2000))
        total += 1

    while min_heap.size() != 1:
        print(min_heap.extract_min())


def find_moving_median_of_numbers(arr):
    left_heap = BinaryHeap()
    right_heap = BinaryHeap()
    print(arr)
    median = 0
    for elem in arr:

        # case 1 if size of left heap is more than right side heap
        if left_heap.size() > right_heap.size():
            if elem > median:
                right_heap.insert_max_heap(elem)
            else:
                # remove from left and add to right
                # add new element to left
                right_heap.insert_min_heap(left_heap.extract_max())
                left_heap.insert_max_heap(elem)
            # Now both heaps are of same size, so median will be the avg of mid
            # elements
            median = (left_heap.get_max() + right_heap.get_min()) / 2

        # case 2 if size of right heap is more than left side heap
        elif left_heap.size() < right_heap.size():
            if elem < median:
                left_heap.insert_max_heap(elem)
            else:
                left_heap.insert_max_heap(right_heap.extract_min())
                right_heap.insert_min_heap(elem)
            median = (left_heap.get_max() + right_heap.get_min()) / 2

        # case 2 if size of right heap is equal to left side heap
        else:
            if elem < median:
                left_heap.insert_max_heap(elem)
                median = left_heap.get_min()
            else:
                right_heap.insert_min_heap(elem)
                median = right_heap.get_max()
        print(median)


print("find_moving_median_of_numbers")
find_moving_median_of_numbers([2, 4, 8, 10, 6, 12, 14])
