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
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.min_heapify(0)
        return minimum

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
        index = self.size()
        self.items.append(key)

        while index != 0:
            parent = self.parent(index)
            if self.get(parent) < self.get(index):
                self.items[index], self.items[parent] = \
                    self.items[parent], self.items[index]
            index = parent

    def insert_min_heap(self, key):
        index = self.size()
        self.items.append(key)

        while index != 0:
            parent = self.parent(index)
            if self.get(parent) > self.get(index):
                self.items[index], self.items[parent] = \
                    self.items[parent], self.items[index]
            index = parent


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
