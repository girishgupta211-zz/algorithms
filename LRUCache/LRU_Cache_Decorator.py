"""
Implement a least recently used (LRU) cache mechanism using a decorator and demonstrate it use in a small script.
The LRU must be able to admit a max_size parameter that by default has to be 100.
"""
from _thread import RLock
from collections import OrderedDict


class LruCache(object):
    """ Decorator cache mechanism """

    def __init__(self, max_size=100):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.lock = RLock()  # because updates aren't threadsafe

    def cache_clean(self):
        with self.lock:
            self.cache.clear()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            kwtuple = tuple(
                (key, kwargs[key]) for key in sorted(kwargs.keys()))
            key = (args, kwtuple)

            # Check if key already exits then update the value and put key in beginning
            with self.lock:
                if key in args:
                    value = self.cache[key]
                    del self.cache[key]
                    self.cache[key] = value
                    return value

            # pop item if it's full in FIFO order
            with self.lock:
                if len(self.cache) == self.max_size:
                    self.cache.popitem(last=False)

            with self.lock:
                value = func(*args, **kwargs)
                self.cache[key] = value
                return value

        wrapper.cache = self.cache
        wrapper.max_size = self.max_size
        wrapper.cache_clean = self.cache_clean
        return wrapper


if __name__ == '__main__':
    """ LRU cache implementation with script"""


    @LruCache(max_size=2)
    def square(x):
        return x * x


    square(2)
    square(3)
    square(4)
    print(square.cache.values())
    assert (4 not in [v for v in square.cache.values()])
    assert (9 in [v for v in square.cache.values()])
    assert (16 in [v for v in square.cache.values()])
    square.cache_clean()
    assert len(square.cache) == 0
