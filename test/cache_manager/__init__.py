from collections import OrderedDict
from functools import wraps

class LRUCache(OrderedDict):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.max_size:
            oldest = next(iter(self))
            del self[oldest]
caches = {}

def cache(func):
    max_size=1024
    if func.__name__ not in caches:
        caches[func.__name__]=LRUCache(max_size)
    @wraps(func)
    def runs(*args, **kwargs):
        if tuple([tuple(args), tuple(kwargs)]) in caches[func.__name__]:
            return caches[func.__name__][tuple([tuple(args), tuple(kwargs)])]
        result = func(*args, **kwargs)
        caches[func.__name__][tuple([tuple(args), tuple(kwargs)])] = result
        return result
    return runs
