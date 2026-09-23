

class Filter:
    def __init__(self, func, iterable):
        self._iterator = iter(iterable)
        self._func = func

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            value = next(self._iterator)
            if self._func(value):
                return value


def filter_(func, iterable):
    for element in iterable:
        if func(element):
            yield element


