"""
Implement a least recently used (LRU) cache mechanism using a decorator and demonstrate it use in a small script.
The LRU must be able to admit a max_size parameter that by default has to be 100.
"""
from collections import OrderedDict
from _thread import RLock


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
            args_keys = tuple((k, kwargs[k]) for k in sorted(kwargs.keys()))
            key = (args, args_keys)

            # Check if key already exits then update the value and put key in beginning
            with self.lock:
                if key in args:
                    val = self.cache[key]
                    del self.cache[key]
                    self.cache[key] = val
                    return val

            # pop item if it's full
            with self.lock:
                if len(self.cache) == self.max_size:
                    self.cache.popitem(last=False)

            with self.lock:
                val = func(*args, **kwargs)
                self.cache[key] = val
                return val

        wrapper.cache = self.cache
        wrapper.max_size = self.max_size
        wrapper.cache_clean = self.cache_clean
        return wrapper


if __name__ == '__main__':
    """ LRU cache implementation with script"""
    cache_size = 2


    @LruCache(max_size=cache_size)
    def add(x, y):
        return x + y


    add(10, y=11)
    add(10, y=12)
    add(10, 15)
    assert (21 not in [v for v in add.cache.values()])
    assert (22 in [v for v in add.cache.values()])
    assert (25 in [v for v in add.cache.values()])
    add.cache_clean()
    assert len(add.cache) == 0
