"""
Implement a least recently used (LRU) cache mechanism using a decorator and demonstrate it use in a small script.
The LRU must be able to admit a max_size parameter that by default has to be 100.
"""
from collections import OrderedDict


class LruCache(object):
    """ Decorator cache mechanism """

    def __init__(self, max_size=100):
        self.cache = OrderedDict()
        self.max_size = max_size

    def cache_clean(self):
        self.cache.clear()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            args_keys = tuple((k, kwargs[k]) for k in sorted(kwargs.keys()))
            key = (args, args_keys)
            if key in args:
                val = self.cache[key]
                del self.cache[key]
                self.cache[key] = val
                return val

            # pop item if it's full
            if len(self.cache) == self.max_size:
                self.cache.popitem(last=False)

            val = func(*args, **kwargs)
            self.cache[key] = val
            return val

        wrapper.cache = self.cache
        wrapper.max_size = self.max_size
        wrapper.cache_clean = self.cache_clean
        return wrapper


if __name__ == '__main__':
    """ LRU cache implementation with script"""
    cacheSize = 2


    @LruCache(max_size=cacheSize)
    def sum(x, y):
        return x + y


    sum(10, y=11)
    sum(10, y=12)
    sum(10, 15)
    assert (21 not in [v for v in sum.cache.values()])
    assert (22 in [v for v in sum.cache.values()])
    assert (25 in [v for v in sum.cache.values()])
    sum.cache_clean()
    assert len(sum.cache) == 0