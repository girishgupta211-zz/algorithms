from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cacheLine = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cacheLine:
            value = self.cacheLine[key]
            del self.cacheLine[key]  # removing from list
            self.cacheLine[key] = value  # adding again to make it most recent
            return value
        else:
            return -1

    def put(self, key, value):

        if key in self.cacheLine:
            del self.cacheLine[key]
        else:
            if len(self.cacheLine) == self.capacity:
                self.cacheLine.popitem(last=False)
        self.cacheLine[key] = value


lruCache = LRUCache(2)
print(lruCache.get(2))
print(lruCache.put(2, 6))
print(lruCache.get(1))
print(lruCache.put(1, 5))
print(lruCache.put(1, 2))
print(lruCache.get(1))
print(lruCache.get(2))
